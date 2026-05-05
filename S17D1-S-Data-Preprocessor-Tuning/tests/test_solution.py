from nbresult import ChallengeResultTestCase

class TestSolution(ChallengeResultTestCase):

    def test_n_best(self):
        res = self.result.n_best
        self.assertEqual(res, 5)
    
    def test_cv_score(self):
        res = self.result.cv_score
        self.assertGreater(res, 0.9)
        self.assertLess(res, 0.95)