import unittest
import io
import contextlib
from unittest.mock import patch
from src.perceptron import Perceptron

from tmc import points

from tmc.utils import load, get_stdout

IMGS_FILE = 'mnist-x.data'
CHARS_FILE = 'mnist-y.data'

perc = Perceptron(IMGS_FILE, CHARS_FILE)


@points('Perceptron')
class MainTest(unittest.TestCase):

    def test_easy(self):
        self.longMessage = False
        best_result = .0
        for i in range(3):
            perc.train('7', '5', 100)
            best_result = max(perc.test('7', '5'), best_result)

        self.assertLess(0.8, best_result,
                           msg='Your algorithm was not good enough. Try to get the failure rate to under 20%.')

    def test_difficult(self):
        self.longMessage = False
        best_result = .0
        for i in range(3):
            perc.train('3', '5', 100)
            best_result = max(perc.test('3', '5'), best_result)

        self.assertLess(0.8, best_result,
                           msg='Your algorithm was not good enough. Try to get the failure rate to under 20%.')
