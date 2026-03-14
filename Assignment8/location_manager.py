"""
Location manager using lists and dictionaries
"""

import unittest


class LocationManager:

    def __init__(self):

        self.locations = []
        self.history = {}

    def add_location(self, location):

        self.locations.append(location)

        if location in self.history:
            self.history[location] += 1
        else:
            self.history[location] = 1


class TestLocationManager(unittest.TestCase):

    def test_add_location(self):

        lm = LocationManager()
        lm.add_location("Chicago")

        self.assertIn("Chicago", lm.locations)

    def test_history(self):

        lm = LocationManager()
        lm.add_location("Chicago")
        lm.add_location("Chicago")

        self.assertEqual(lm.history["Chicago"], 2)


if __name__ == "__main__":
    unittest.main()