import unittest
from initial_exercise.sum_of_three import sum3


class TestSumOfThree(unittest.TestCase):
    def test_numbers_0_0_0(self):
        self.assertEqual(sum3(0, 0, 0), 0)

    def test_numbers_1_2_3(self):
        self.assertEqual(sum3(1, 2, 3), 6)

if __name__ == "__main__":
    unittest.main()