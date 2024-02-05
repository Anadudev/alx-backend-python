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
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, log: Dict, mocker: MagicMock) -> None:
        """_summary_

        Args:
            org (str): _description_
            log (Dict): _description_
            mocker (MagicMock): _description_
        """
        mocker.return_value = MagicMock(return_value=log)
        github_client = GithubOrgClient(org)
        self.assertEqual(github_client.org(), log)
        mocker.assert_called_once_with(f"https://api.github.com/orgs/{org}")
