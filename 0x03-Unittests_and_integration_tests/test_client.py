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
            ("google"),
            ("abc"),
        ]
    )
    @patch(
            "client.get_json", return_value{"payload": True},
    )
    def test_org(self, org: str, mocker: MagicMock) -> None:
        """_summary_

        Args:
            org (str): _description_
            mocker (MagicMock): _description_
        """
        github_client = GithubOrgClient(org)
        ret_val = github_client.org
        self.assertEqual(ret_val, mocker.ret_val)
        mocker.assert_called_once
