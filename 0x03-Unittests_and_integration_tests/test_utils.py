#!/usr/bin/env python3
"""_summary_
"""
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, output):
        """_summary_"""
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """testing for function assertion"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Mock http calls"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("test_utils.get_json")
    def test_get_json(self, url, payload, mock_get):
        """testing return data of get_json method"""
        mock_get.return_value = payload
        result = get_json(url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """testing the memoize method"""

    def test_memoize(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        class TestClass:
            """_summary_"""

            def a_method(self):
                """_summary_

                Returns:
                    _type_: _description_
                """
                return 42

            @memoize
            def a_property(self):
                """_summary_

                Returns:
                    _type_: _description_
                """
                return self.a_method()

        with patch.object(
            TestClass,
            "a_method",
            return_value=lambda: 42,
        ) as pp:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            pp.assert_called_once()
