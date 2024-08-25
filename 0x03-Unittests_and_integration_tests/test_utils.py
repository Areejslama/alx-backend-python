#!/usr/bin/env python3
"""define test case"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """define class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """define function"""
        maps = access_nested_map(nested_map, path)
        self.assertEqual(maps, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(
            self, nested_map, path, exception
            ):
        """Test that an exception is raised"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """define class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url, test_payload):
        json = {'json.return_value': test_payload}
        with patch('requests.get', return_value=Mock(**json)) as request:
            self.assertEqual(get_json(test_url), test_payload)
            request.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test the memoize decorator."""
    def test_memoize(self):
        """Test that memoization works as expected."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                'a_method',
                return_value=lambda: 42,
                ) as memo:
            test = TestClass()
            self.assertEqual(test.a_property(), 42)
            self.assertEqual(test.a_property(), 42)
            memo.assert_called_once()


if __name__ == "__main__":
    unittest.main()
