import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestOrderCumulativeAmountPerCustomer(ChallengeResultTestCase):
    db_path = os.path.join(os.path.dirname(__file__), '../data/ecommerce.sqlite')

    def query_db(self, query, *args):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute(query, args)
        results = db.fetchall()
        return results

    def test_query_order_cumulative_amount_per_customer(self):
        result = self.query_db(self.result.query)
        expected = [
                (1, 1, "2012-01-04", 3.75),
                (8, 1, "2012-06-13", 17.25),
                (12, 1, "2012-09-13", 30.25),
                (2, 2, "2012-01-27", 7.25),
                (4, 2, "2012-03-13", 20.75),
                (9, 2, "2012-07-06", 25.5),
                (14, 2, "2012-10-29", 33.0),
                (19, 2, "2013-02-21", 47.0),
                (6, 3, "2012-04-28", 11.0),
                (10, 3, "2012-07-29", 18.75),
                (11, 3, "2012-08-21", 30.25),
                (16, 3, "2012-12-14", 44.25),
                (18, 3, "2013-01-29", 55.0),
                (20, 3, "2013-03-16", 60.5),
                (3, 4, "2012-02-19", 5.5),
                (5, 4, "2012-04-05", 14.25),
                (7, 4, "2012-05-21", 25.5),
                (15, 4, "2012-11-21", 33.75),
                (13, 5, "2012-10-06", 12.25),
                (17, 5, "2013-01-06", 18.5)
        ]
        self.assertIs(type(result), list)
        self.assertIs(type(result[0]), tuple)
        self.assertEqual(len(result), len(expected))
        self.assertEqual(result[0], expected[0])
        self.assertEqual(result[-1], expected[-1])