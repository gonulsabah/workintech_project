from nbresult import ChallengeResultTestCase


class TestTrainingData(ChallengeResultTestCase):
    def test_price_and_freight(self):
        columns = ['delay_vs_expected',
                   'dim_is_five_star',
                   'dim_is_one_star',
                   'expected_wait_time',
                   'freight_value',
                   'number_of_items',
                   'number_of_sellers',
                   'order_id',
                   'order_status',
                   'price',
                   'review_score',
                   'wait_time']
        self.assertEqual(self.result.columns, columns)