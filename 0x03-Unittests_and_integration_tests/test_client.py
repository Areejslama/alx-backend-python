#!/usr/bin/env python3
"""this script to test methods"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from test_utils import TestGetJson
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """define class"""
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, value, mock):
        """define function"""
        client = GithubOrgClient(value)
        client.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{value}')

    def test_public_repos_url(self):
        """define function"""
        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock
                ) as mock:
            payload = "World"
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload)
