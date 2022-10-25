import unittest
import io
import contextlib
from unittest.mock import patch
from src.spamham import SpamHam

from tmc import points

from tmc.utils import load, get_stdout

HAM_FILE = 'hamcount.txt'
SPAM_FILE = 'spamcount.txt'
SPAM_MESSAGE = 'spamesim.txt'
HAM_MESSAGE = 'hamesim.txt'

antispambot = SpamHam(SPAM_FILE, HAM_FILE)


@points('SpamHam')
class MainTest(unittest.TestCase):

    def test_spam(self):
        self.longMessage = False
        self.assertAlmostEqual(1.0, antispambot.evaluate_from_file(SPAM_MESSAGE), delta=0.1,
                               msg='Spam is not detected')

    def test_ham(self):
        self.longMessage = False
        self.assertAlmostEqual(0.0, antispambot.evaluate_from_file(HAM_MESSAGE), delta=0.1,
                               msg='Ham is not detected')
