import unittest

from process.top_scores import increment_count


class TestLoaders(unittest.TestCase):
    def test_increment_count(self):
        test = {'a': 1}
        test = increment_count(test, 'a')
        self.assertEqual(test, {'a': 2})
        test = increment_count(test, 'b')
        self.assertEqual(test, {'a': 2, 'b': 1})


if __name__ == '__main__':
    unittest.main()
