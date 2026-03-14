"""
Weather application (simplified)
"""

import unittest


class WeatherApp:
    """Tracks weather locations"""

    def __init__(self):
        self.locations = []
        self.history = {}

    def add_location(self, location):
        self.locations.append(location)
        self.history[location] = self.history.get(location, 0) + 1


class TestWeatherApp(unittest.TestCase):

    def test_add_location(self):
        app = WeatherApp()
        app.add_location("Chicago")
        self.assertIn("Chicago", app.locations)

    def test_history_dictionary(self):
        app = WeatherApp()
        app.add_location("Chicago")
        app.add_location("Chicago")
        self.assertEqual(app.history["Chicago"], 2)


if __name__ == "__main__":
    unittest.main()