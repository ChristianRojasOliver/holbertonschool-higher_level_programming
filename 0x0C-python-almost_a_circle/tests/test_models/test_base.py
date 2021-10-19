#!/usr/bin/python3
"""Unitest for base class"""


import unittest
from models.base import Base

class TestBase(unittest.Test):
    """Unittest for Base"""
    @classmethod
    def setUp:
        self.one = Base(1)

    def testid:
        self.assertEqual(self.one.id, 1)
