from nbresult import ChallengeResultTestCase


class TestDecisionThreshold(ChallengeResultTestCase):
    def test_decision_threshold(self):
        self.assertLess(self.result.threshold, 0.9)
        self.assertGreater(self.result.threshold, 0.8)
