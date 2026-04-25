# pylint: disable-all
import unittest

from farm.animal import Animal
from farm.cow import Cow
from farm.chicken import Chicken


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal = Animal()

    def test_initialize_sets_energy_to_zero(self):
        """Test that Animal's energy is initialized to 0."""
        self.assertEqual(self.animal.energy, 0)

    def test_feed_increases_energy(self):
        """Test that feed! increases Animal's energy by 1."""
        self.animal.feed()
        self.assertEqual(self.animal.energy, 1)


class TestCow(unittest.TestCase):
    def setUp(self):
        self.cow = Cow()

    def test_cow_inherits_animal(self):
        """Test that Cow inherits from Animal."""
        self.assertTrue(issubclass(Cow, Animal))


class TestChicken(unittest.TestCase):
    def setUp(self):
        self.chicken = Chicken("male")

    def test_chicken_inherits_animal(self):
        """Test that Chicken inherits from Animal."""
        self.assertTrue(issubclass(Chicken, Animal))