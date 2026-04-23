from nbresult import ChallengeResultTestCase


class TestSolvers(ChallengeResultTestCase):
    def test_fastest_solver(self):
        self.assertEqual(self.result.fastest_solver, "lbfgs")
