import unittest
from Exercises.city import formattedCity

class TestCity(unittest.TestCase):
    def test_city_country(self):
        city = formattedCity('santiago', 'chile')
        self.assertEqual(city, 'Santiago, Chile')

    """ def test_city_country_population(self):
        city = formattedCity('santiago', 'chile', 5000000)
        self.assertEqual(city, 'Santiago, Chile - population 5000000') """