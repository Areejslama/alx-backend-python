#!/usr/bin/env python3
"""define test case"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock
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
    """ Class for Testing Memoize """

    def test_memoize(self):
        """ Test that when calling a_property twice, the correct result
        is returned but a_method is only called once using
        assert_called_once
        """

        class TestClass:
            """ Test Class for wrapping with memoize """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock_method.assert_called_once()
