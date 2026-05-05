import nbresult
from nbresult import ChallengeResultTestCase


class TestPipe(ChallengeResultTestCase):
    """Test suite for validating the pipeline output and behavior."""

    def test_pipe_not_crashing(self):
        """Test that the pipeline does not crash and has the correct output shape and columns."""
        self.assertNotEqual(self.result.shape[1], 32,
                            msg="Too many columns. Remember to drop the second column when encoding binary features.")
        self.assertEqual(self.result.shape, (1000, 31))

    def test_pipe_result_exists(self):
        """Test that the result attribute exists and is not None."""
        self.assertIsNotNone(getattr(self, 'result', None), msg="The result attribute should not be None.")