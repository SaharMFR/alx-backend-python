#!/usr/bin/env python3
""" Unittests and Integration Tests """
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Tests `utils.access_nested_map` function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Tests `access_nested_map` """
        self.assertEqual(access_nested_map(nested_map, path), expected)
