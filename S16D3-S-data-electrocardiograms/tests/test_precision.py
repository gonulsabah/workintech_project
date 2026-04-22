from nbresult import ChallengeResultTestCase


class TestPrecision(ChallengeResultTestCase):
    def test_precision(self):
        self.assertEqual(self.result.precision,  0.94)