import unittest

from pathlib import Path
from loaders.loaders import load_file


class TestLoaders(unittest.TestCase):
    def test_load_file(self):
        file_path = Path('tests/data/sample.txt')
        expected_output = ['1', '2', '3', '4', '5']
        self.assertEqual(load_file(file_path), expected_output)


if __name__ == '__main__':
    unittest.main()
