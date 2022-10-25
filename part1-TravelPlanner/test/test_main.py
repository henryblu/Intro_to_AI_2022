import unittest
import io
import contextlib
from unittest.mock import patch
from src.citymap import CityMap

from tmc import points

from tmc.utils import load, get_stdout

FIRST_OUTPUT = '1121480 -> 1121438 -> 1220414 -> 1220416 -> 1220418 -> 1220420 -> 1220426 -> 1173416' + \
               ' -> 1173423 -> 1250425 -> 1250427 -> 1250429'
SECOND_OUTPUT = '1220425 -> 1220406 -> 1121436 -> 1113434 -> 1113432 -> 1111428 -> 1010427'


@points('TravelPlanner')
class MainTest(unittest.TestCase):
    def test_01_prints_correct_value(self):
        self.longMessage = False
        citymap = CityMap("network.json")
        results = str(citymap.search("1250429", "1121480"))
        self.assertEqual(FIRST_OUTPUT, results)

    def test_02_prints_correct_value(self):
        self.longMessage = False
        citymap = CityMap("network.json")
        results = str(citymap.search("1010427", "1220425"))
        self.assertEqual(SECOND_OUTPUT, results)


