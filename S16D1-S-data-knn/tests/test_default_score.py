from nbresult import ChallengeResultTestCase


class TestDefaultScore(ChallengeResultTestCase):
    def test_default_score(self):
        self.assertGreater(self.result.score, 0.55)