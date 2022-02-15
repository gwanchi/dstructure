"""
Implement an algorithm to determine if a string has all unique characters.
"""
import unittest


class UniqueChars(object):
    def has_unique_chars(self, string):
        if string is None:
            return False
        return len(set(string)) == len(string)

    def has_unique_chars2(self, string):
        if string is None:
            return False
        chars_set = set()
        for char in string:
            if char in chars_set:
                return False
            else:
                chars_set.add(char)
        return True

    def has_unique_char3(self, string):
        if string is None:
            return False
        for char in string:
            if string.count(char) > 1:
                return False
        return True


class TestUniqueChars(unittest.TestCase):
    def test_unique_chars(self, func):
        self.assertEqual(func(None), False)
        self.assertEqual(func(''), True)
        self.assertEqual(func('foo'), False)
        self.assertEqual(func('bar'), True)
        print('Success: test_unique_chars')


def main():
    test = TestUniqueChars()
    unique_chars = UniqueChars()
    test.test_unique_chars(unique_chars.has_unique_chars)


if __name__ == '__main__':
    main()
