"""
Weather API class (mock version)
"""

import unittest


class WeatherAPI:

    def get_weather(self, location):

        return {
            "location": location,
            "temperature": 20,
            "condition": "Sunny"
        }


class TestWeatherAPI(unittest.TestCase):

    def test_weather_data(self):

        api = WeatherAPI()
        data = api.get_weather("Chicago")

        self.assertEqual(data["location"], "Chicago")


if __name__ == "__main__":
    unittest.main()