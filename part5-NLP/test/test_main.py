import unittest
import io
import contextlib
from unittest.mock import patch
import os
import spacy
from tmc import points

from tmc.utils import load, get_stdout


@points('NLP')
class MainTest(unittest.TestCase):

    def test_easy(self):
        assert(True)
