import unittest
from farm.chicken import Chicken


class TestChicken(unittest.TestCase):

    def setUp(self):
        self.female_chicken = Chicken('female')
        self.male_chicken = Chicken('male')

    def test_initialize_sets_eggs_to_zero(self):
        """Test that Chicken's eggs are initialized to 0."""
        self.assertEqual(self.female_chicken.eggs, 0)

    def test_initialize_sets_gender(self):
        """Test that Chicken's gender is set correctly."""
        self.assertEqual(self.male_chicken.gender, "male")
        self.assertEqual(self.female_chicken.gender, "female")

    def test_initialize_sets_energy_to_zero(self):
        """Test that Chicken's energy is initialized to 0."""
        self.assertEqual(self.male_chicken.energy, 0)
        self.assertEqual(self.female_chicken.energy, 0)

    def test_feed_extends_method(self):
        """Test that Chicken has a feed method."""
        self.assertTrue(hasattr(self.female_chicken, 'feed'))

    def test_feed_adds_eggs_for_female(self):
        """Test that feeding a female chicken adds 2 eggs."""
        self.female_chicken.feed()
        self.assertEqual(self.female_chicken.eggs, 2)
        self.female_chicken.feed()
        self.assertEqual(self.female_chicken.eggs, 4)

    def test_feed_does_not_add_eggs_for_male(self):
        """Test that feeding a male chicken does not add eggs."""
        self.male_chicken.feed()
        self.assertEqual(self.male_chicken.eggs, 0)

    def test_feed_adds_energy(self):
        """Test that feeding a chicken adds 1 energy."""
        self.female_chicken.feed()
        self.assertEqual(self.female_chicken.energy, 1)
        self.male_chicken.feed()
        self.assertEqual(self.male_chicken.energy, 1)

    def test_talk_returns_correct_sound(self):
        """Test that the talk method returns the correct sound."""
        self.assertEqual(self.male_chicken.talk(), "cock-a-doodle-doo")
        self.assertEqual(self.female_chicken.talk(), "cluck cluck")