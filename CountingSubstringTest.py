from CountingSubstring import count_substring
import unittest

class CountingSubstringTest(unittest.TestCase): # Use camel case for naming classes; no underscore, must have Title case
    def test(self):
        self.assertEqual(0, count_substring("ABCDCDC", "cdc"))
        self.assertEqual(0, count_substring("ABCDCDC", "popo"))
        self.assertEqual(3, count_substring("pizza pizza pizza", "pizza"))
        self.assertEqual(2, count_substring("pizza pizza pizza", " "))
        self.assertNotEqual(None, count_substring("ABCD", "popo"))

if __name__ == "__main__":
    unittest.main()