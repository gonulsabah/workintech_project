import numpy as np
import pandas as pd
from olist.data import Olist
from olist.utils import haversine_distance

class Order():
    def __init__(self):
        self.olist = Olist()
        self.data = self.olist.get_data()
    
    def get_wait_time(self, is_delivered=True):
        # order_id, wait_time, expected_wait_time, delay_vs_expected, order_status
        if is_delivered:
            orders = self.data['orders'].query("order_status=='delivered'").copy()
        else:
            orders = self.data['orders'].copy()

        orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
        orders["order_delivered_carrier_date"] = pd.to_datetime(orders["order_delivered_carrier_date"])
        orders["order_delivered_customer_date"] = pd.to_datetime(orders["order_delivered_customer_date"])
        orders["order_estimated_delivery_date"] = pd.to_datetime(orders["order_estimated_delivery_date"])
        
        one_day_delta = np.timedelta64(24, 'h')
        orders.loc[:,'wait_time'] = \
            (orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']) / one_day_delta
            
        orders.loc[:,'delay_vs_expected'] = \
            (orders['order_delivered_customer_date'] - orders['order_estimated_delivery_date']) / one_day_delta
            
        orders.loc[:,'expected_wait_time'] = \
            (orders['order_estimated_delivery_date'] - orders['order_purchase_timestamp']) / one_day_delta
            
        def handle_delay(x):
            if x > 0:
                return x
            else:
                return 0

        orders.loc[:,'delay_vs_expected'] = orders['delay_vs_expected'].apply(handle_delay)
        
        return orders[[
            'order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected',
            'order_status'
        ]]
    
    def get_review_score(self):
        # ["order_id", "dim_is_five_star", "dim_is_one_star", "review_score"]
        reviews = self.data['order_reviews'].copy()
        one_star = lambda x: int(x==1)
        five_star = lambda x: int(x==5)
        
        reviews["dim_is_five_star"] = reviews["review_score"].map(five_star) # --> Series([0, 1, 1, 0, 0, 1 ...])
        reviews["dim_is_one_star"] = reviews["review_score"].map(one_star)
        
        return reviews[["order_id", "dim_is_five_star", "dim_is_one_star", "review_score"]]
    
    def get_number_items(self):
        #   order_id, number_of_items (sipariş başına toplam ürün sayısı)
        data = self.data
        items = (
                data["order_items"]
                .groupby("order_id")
                .size()
                .reset_index(name="number_of_items")
                .sort_values("number_of_items", ascending=False)
            )
        return items

    def get_number_sellers(self):
        # order_id, number_of_sellers (sipariş başına benzersiz satıcıların toplam sayısı)
        data = self.data

        sellers = \
            data['order_items']\
            .groupby('order_id')['seller_id'].nunique().reset_index()
        sellers.columns = ['order_id', 'number_of_sellers']
        sellers.sort_values('number_of_sellers')
        return sellers

    def get_price_and_freight(self):
        # order_id, price, freight_value
        data = self.data
        price_freight = \
            data['order_items']\
            .groupby('order_id',
                    as_index=False).agg({'price': 'sum',
                                        'freight_value': 'sum'})
        return price_freight

    def get_training_data(self, is_delivered=True, with_distance_seller_customer=False):
        """
        Returns a clean DataFrame (without NaN), with the all following columns:
        ['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected',
        'order_status', 'dim_is_five_star', 'dim_is_one_star', 'review_score',
        'number_of_items', 'number_of_sellers', 'price', 'freight_value',
        'distance_seller_customer']
        """
        training_data = self.get_wait_time(is_delivered)\
            .merge(self.get_review_score(), on="order_id")\
                .merge(self.get_number_items(), on="order_id")\
                    .merge(self.get_number_sellers(), on="order_id")\
                        .merge(self.get_price_and_freight(), on="order_id")
        
        if with_distance_seller_customer:
            training_data = training_data.merge(
                self.get_distance_seller_customer(), on='order_id')
        
        return training_data.dropna()
    
    def get_distance_seller_customer(self):
        """
        Returns a DataFrame with:
        order_id, distance_seller_customer
        """
        # $CHALLENGIFY_BEGIN

        # import data
        data = self.data
        orders = data['orders']
        order_items = data['order_items']
        sellers = data['sellers']
        customers = data['customers']

        # Since one zip code can map to multiple (lat, lng), take the first one
        geo = data['geolocation']
        geo = geo.groupby('geolocation_zip_code_prefix',
                          as_index=False).first()

        # Merge geo_location for sellers
        sellers_mask_columns = [
            'seller_id', 'seller_zip_code_prefix', 'geolocation_lat', 'geolocation_lng'
        ]

        sellers_geo = sellers.merge(
            geo,
            how='left',
            left_on='seller_zip_code_prefix',
            right_on='geolocation_zip_code_prefix')[sellers_mask_columns]

        # Merge geo_location for customers
        customers_mask_columns = ['customer_id', 'customer_zip_code_prefix', 'geolocation_lat', 'geolocation_lng']

        customers_geo = customers.merge(
            geo,
            how='left',
            left_on='customer_zip_code_prefix',
            right_on='geolocation_zip_code_prefix')[customers_mask_columns]

        # Match customers with sellers in one table
        customers_sellers = customers.merge(orders, on='customer_id')\
            .merge(order_items, on='order_id')\
            .merge(sellers, on='seller_id')\
            [['order_id', 'customer_id','customer_zip_code_prefix', 'seller_id', 'seller_zip_code_prefix']]

        # Add the geoloc
        matching_geo = customers_sellers.merge(sellers_geo,
                                            on='seller_id')\
            .merge(customers_geo,
                   on='customer_id',
                   suffixes=('_seller',
                             '_customer'))
        # Remove na()
        matching_geo = matching_geo.dropna()

        matching_geo.loc[:, 'distance_seller_customer'] =\
            matching_geo.apply(lambda row:
                               haversine_distance(row['geolocation_lng_seller'],
                                                  row['geolocation_lat_seller'],
                                                  row['geolocation_lng_customer'],
                                                  row['geolocation_lat_customer']),
                               axis=1)
        # Since an order can have multiple sellers,
        # return the average of the distance per order
        order_distance =\
            matching_geo.groupby('order_id',
                                 as_index=False).agg({'distance_seller_customer':
                                                      'mean'})

        return order_distance