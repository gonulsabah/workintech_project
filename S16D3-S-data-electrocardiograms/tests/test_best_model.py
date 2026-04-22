from nbresult import ChallengeResultTestCase


class TestBestModel(ChallengeResultTestCase):
    def test_best_model(self):
        self.assertEqual(self.result.model, "KNN")
