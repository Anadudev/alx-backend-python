#!/usr/bin/env python3
"""_summary_
"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    @parameterized.expand(
        [
            ("google", {'login': "google"}),
            ("abc", {'login': "abc"}),
        ]
    )
    @patch(
            "client.get_json",
    )
    def test_org(self, org: str, exp: Dict, mocker: MagicMock) -> None:
        """_summary_

        Args:
            org (str): _description_
            mocker (MagicMock): _description_
        """
        mocker = MagicMock(return_value=expp)
        github_client = GithubOrgClient(org)
        self.assertEqual(git_client.org, exp)
        mocker.assert_called_once_with(
                f"https://api.github.com/orgs/{org}"
                )
                

    def test_public_repos_url(self) -> None:
        """ Mocking a property """
        with patch(
                "client.GithubOrgClient.org",
                prop_mock=PropertyMock,
                ) as mocker:
            mock_org.return_value = {
                    'repos_url': "https://api.github.com/users/google/repos",
                    }
            self.assertEqual(
                    GithubOrgClient("google").__public_repos_url,
                    "https://api.github.com/users/google/repos",
                    )

    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """  More patching """
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient.__public_repos_url",
                new_callable=PropertyMock,
                ) as mock_repos_url:
            mock_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                    GithubOrgClient("google").public_repos(),
                    ["episodes.dart", "kratu"],
                    )
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once()
    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
        ])
    def test_has_license(self, repo: Dict, key: str, result: bool) -> None:
        """ Parameterize """
        git_client = GithubOrgClient("google")
        client_licence = git_client.has_license(repo, key)
        self.assertEqual(client_licence, result)
