import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestGetOrdersRange(ChallengeResultTestCase):
    db_path = os.path.join(os.path.dirname(__file__), '../data/ecommerce.sqlite')

    def query_db(self, query, *args):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute(query, args)
        results = db.fetchall()
        return results

    def test_type_results(self):
        start_date = "2012-01-04"
        end_date = "2012-03-04"
        results = self.query_db(self.result.query, start_date, end_date)
        self.assertIsInstance(results, list)
    
    def test_len_results(self):
        date_from = "2012-01-04"
        date_to = "2012-03-04"
        results = self.query_db(self.result.query, date_from, date_to)
        self.assertEqual(len(results), 2)