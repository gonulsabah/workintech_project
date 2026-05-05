import pandas as pd
import numpy as np
from nbresult import ChallengeResultTestCase


class TestPrediction(ChallengeResultTestCase):
    """Test prediction output for expected value range and type."""

    def test_prediction(self):
        """Test that the prediction is within the expected value range."""
        res = self.result.prediction
        if isinstance(res, (pd.Series, np.ndarray, list)):
            res = list(res)[0]
        self.assertGreaterEqual(res, 15)
        self.assertLess(res, 25)

    def test_prediction_type(self):
        """Ensure prediction is a numeric type."""
        res = self.result.prediction
        if isinstance(res, (pd.Series, np.ndarray, list)):
            res = list(res)[0]
        self.assertIsInstance(res, (int, float, np.integer, np.floating))