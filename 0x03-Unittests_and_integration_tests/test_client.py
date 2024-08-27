#!/usr/bin/env python3
"""this script to test methods"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
import json
from unittest.mock import patch, PropertyMock, Mock


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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Test that the list of repos"""
        json = [{"name": "Hello"}, {"name": "Summer"}]
        mock_json.return_value = json

        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock
                )as mock:
            mock.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json]
            self.assertEqual(result, check)

            mock.assert_called_once()
            mock_json.assert_called_once()
 
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """define function"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
