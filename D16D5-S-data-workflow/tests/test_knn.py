from nbresult import ChallengeResultTestCase


class TestKnn(ChallengeResultTestCase):
    def test_best_k(self):
        self.assertGreaterEqual(self.result.best_k, 10)
        self.assertLessEqual(self.result.best_k, 25)
    
    def test_best_score(self):
        self.assertEqual(round(self.result.best_score, 2),  0.76)