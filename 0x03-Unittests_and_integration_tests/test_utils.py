#!/usr/bin/env python3
"""define test case"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


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
            ({"a": 1}, ("a", "b"), KeyError)
        ])
        def test_access_nested_map_exception(
                self, nested_map, path, exception
        ):
            """Test that an exception is raised"""
            with self.assertRaises(exception):
                access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
