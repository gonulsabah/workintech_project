from nbresult import ChallengeResultTestCase


class TestEncoding(ChallengeResultTestCase):
    def test_aspiration(self):
        self.assertEqual(self.result.dataset.aspiration.max(), 1)
    def test_enginelocation(self):
        self.assertEqual(self.result.dataset.enginelocation.max(), 1)
    def test_enginetype(self):
        with_enginetype_count = 0
        for col in self.result.dataset.columns:
            if col.startswith("enginetype"):
                with_enginetype_count += 1
        self.assertEqual(with_enginetype_count == 7, True)
        self.assertEqual(len(self.result.dataset.columns) > 13, True)
    def test_cylindernumber(self):
        self.assertEqual(self.result.dataset.cylindernumber.max(), 8)
    def test_price(self):
        self.assertEqual(self.result.dataset.price.max(), 1)