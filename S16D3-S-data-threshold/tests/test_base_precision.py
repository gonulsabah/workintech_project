from nbresult import ChallengeResultTestCase


class TestBasePrecision(ChallengeResultTestCase):
    def test_base_precision(self):
        self.assertLess(self.result.score, 0.8)
        self.assertGreater(self.result.score, 0.4)
