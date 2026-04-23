from nbresult import ChallengeResultTestCase


class TestBaseModel(ChallengeResultTestCase):
    def test_base_model_score(self):
        self.assertEqual(self.result.score > 0.8, True)    