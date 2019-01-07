"""
# test demo.foobar

@author: Jinchi Zhang
@email: jizjiz148148@gmail.com

"""
import unittest
from jinchi.demo.foobar import check_env


class TryTest(unittest.TestCase):
    """
    TryTest includes all unit tests for try.py
    """

    def setUp(self):
        pass

    def test_check_env(self):
        """
        test check_env
        """
        import os
        os.environ["NUMBER"] = "1"
        os.environ["VAL"] = "some string"

        tests = [
            {
                "category": "normal",
                "cases": [
                    {"input": "DOES_NOT_EXIST_AT_ALL", "expected": "None"},
                    {"input": "NUMBER", "expected": "Integer"},
                    {"input": "VAL", "expected": "String"},
                ]
            },
            {
                "category": "edge",
                "cases": [
                    {"input": 1, "expected": "None"},
                    {"input": {}, "expected": "None"},
                ]
            }
        ]
        for cat in tests:
            category = cat['category']
            cases = cat['cases']
            for test in cases:
                result = check_env(test['input'])
                self.assertEqual(result, test['expected'])
        pass
