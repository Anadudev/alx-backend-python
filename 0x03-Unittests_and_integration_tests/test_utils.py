#!/usr/bin/env python3
"""_summary_
"""
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def test_access_nested_map(self):
        """_summary_"""
        myMap = {"a": {"b": {"c": {"d": 5}}}}
        self.assertRaises(KeyError, access_nested_map(myMap, 12))
        self.assertEqual(access_nested_map(myMap, ["a", "b", "c", "d"]), 5)


if __name__ == "__main__":
    unittest.main()
