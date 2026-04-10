from nbresult import ChallengeResultTestCase


class TestNumberSellers(ChallengeResultTestCase):
    def test_number_sellers(self):
        self.assertEqual(self.result.shape, (98666, 2))
        self.assertEqual(self.result.columns, ["order_id", "number_of_sellers"])