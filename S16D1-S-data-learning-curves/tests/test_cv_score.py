from nbresult import ChallengeResultTestCase


class TestCvScore(ChallengeResultTestCase):
    def test_cv_score(self):
        self.assertLess(self.result.score, 0.6)
        self.assertGreater(self.result.score, 0.5)