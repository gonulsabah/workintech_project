from nbresult import ChallengeResultTestCase


class TestStrong_model(ChallengeResultTestCase):
    def test_strong_model(self):
        self.assertEqual(self.result.score > 0.86, True)