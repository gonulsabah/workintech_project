from nbresult import ChallengeResultTestCase


class TestPriceError(ChallengeResultTestCase):
    def test_price_error(self):
        self.assertTrue(25000 < abs(self.result.error) < 35000)