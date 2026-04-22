from nbresult import ChallengeResultTestCase


class TestPrediction(ChallengeResultTestCase):
    def test_prediction(self):
        self.assertEqual(self.result.prediction,  "at risk")