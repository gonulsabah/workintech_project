from nbresult import ChallengeResultTestCase


class TestNumberItems(ChallengeResultTestCase):
    def test_number_items(self):
        self.assertEqual(self.result.shape, (98666, 2))
        self.assertEqual(self.result.columns, ["order_id", "number_of_items"])