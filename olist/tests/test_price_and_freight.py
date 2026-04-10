from nbresult import ChallengeResultTestCase


class TestPriceAndFreight(ChallengeResultTestCase):
    def test_price_and_freight(self):
        self.assertEqual(self.result.shape, (98666, 3))
        self.assertEqual(self.result.columns, ["order_id","price", "freight_value"])