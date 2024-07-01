#!/usr/bin/env python3
""" Unittests and Integration Tests """
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Sequence, Union, Dict
from unittest.mock import patch
import requests


class TestAccessNestedMap(unittest.TestCase):
    """ Tests `utils.access_nested_map` function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Union[Dict, int]) -> None:
        """ Tests `access_nested_map` """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         exception: Exception) -> None:
        """ Tests KeyError exceptions of `access_nested_map` """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Tests `utils.get_json` function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """ Tests `get_json` """
        with patch("requests.get") as request:
            request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """ Tests `utils.memoize` function """
    def test_memoize(self) -> None:
        """ Tests `memoize` """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method") as memo:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            memo.assert_called_once()
