#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Japanese regular expression samples
"""

import re
import unittest

re_hiragana = re.compile(r'[\u3041-\u3093]+')
re_katakana = re.compile(r'[\u30A1-\u30F4]+')

def is_hiragana(input_str):
    return re_hiragana.fullmatch(input_str) is not None

def is_katakana(input_str):
    return re_katakana.fullmatch(input_str) is not None


class TestJapaneseRegexMethods(unittest.TestCase):
    def test_is_hiragana(self):
        self.assertEqual(is_hiragana("あいうえお"), True)
        self.assertEqual(is_hiragana("アイウエオ"), False)
        self.assertEqual(is_hiragana("漢字"), False)

    def test_is_katakana(self):
        self.assertEqual(is_katakana("アイウエオ"), True)
        self.assertEqual(is_katakana("あいうえお"), False)
        self.assertEqual(is_katakana("漢字"), False)

if __name__ == "__main__":
    unittest.main()
