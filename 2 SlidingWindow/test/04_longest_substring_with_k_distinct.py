import unittest


class TestLongestSubstringWithKDistinct(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(longest_substring_with_k_distinct("araaci", 2), 4)
        self.assertEqual(longest_substring_with_k_distinct("cbbebi", 3), 5)

    def test_empty_string(self):
        self.assertEqual(longest_substring_with_k_distinct("", 3), 0)

    def test_single_char_string(self):
        self.assertEqual(longest_substring_with_k_distinct("aaaaa", 1), 5)

    def test_k_greater_than_string_length(self):
        self.assertEqual(longest_substring_with_k_distinct("abc", 5), 3)

    def test_k_zero(self):
        self.assertEqual(longest_substring_with_k_distinct("abc", 0), 0)

    def test_k_negative(self):
        self.assertEqual(longest_substring_with_k_distinct("abc", -1), 0)

if __name__ == '__main__':
    unittest.main()