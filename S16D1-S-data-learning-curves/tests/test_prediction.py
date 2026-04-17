from nbresult import ChallengeResultTestCase


class TestPrediction(ChallengeResultTestCase):
    def test_prediction(self):
        self.assertLess(self.result.poly_3_score, self.result.feat_3_score)