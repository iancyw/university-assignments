import unittest
from assignment1 import find_rotations


class TestFindRotations(unittest.TestCase):
    def test_given(self):
        string_list = [
            'aaa',
            'abc',
            'cab',
            'acb',
            'wxyz',
            'yzwx',
        ]
        p = 1
        expected = [
            'aaa',
            'cab',
        ]
        self.assertEqual(find_rotations(string_list, p), expected)

    def test_two_rotations(self):
        string_list = [
            'aaa',
            'abc',
            'cab',
            'acb',
            'wxyz',
            'yzwx',
        ]
        p = 2
        expected = [
            'aaa',
            'abc',
            'yzwx',
            'wxyz',
        ]
        self.assertEqual(find_rotations(string_list, p), expected)

    def test_negative(self):
        string_list = [
            'aaa',
            'abc',
            'cab',
            'acb',
            'wxyz',
            'yzwx',
        ]
        p = -1
        expected = [
            'aaa',
            'abc',
        ]
        self.assertEqual(find_rotations(string_list, p), expected)

    def test_empty_list(self):
        for i in range(-3, 4):
            self.assertEqual(find_rotations([], i), [])

    def test_empty_string(self):
        for i in range(-3, 4):
            self.assertEqual(find_rotations([''], i), [''])

    def test_empty_string_among_nonempty(self):
        string_list = [
            'aaa',
            'abc',
            '',
            'cab',
        ]
        p = 2
        expected = [
            '',
            'aaa',
            'abc',
        ]
        self.assertEqual(find_rotations(string_list, p), expected)

    def test_different_lengths(self):
        # By Zi Li Tan https://lms.monash.edu/mod/forum/discuss.php?d=1861606
        string_list = [
            'qwertyui',
            'wertyuiq',
            'rtyuiqwe',
            'asdfgh',
            'dfghas',
        ]
        p = 2
        expected = [
            'asdfgh',
            'wertyuiq',
        ]
        self.assertEqual(find_rotations(string_list, p), expected)


if __name__ == '__main__':
    unittest.main()
