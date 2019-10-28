import unittest

import pandas as pd

from process.helpers import dict_to_df, increment_count, init_zero_dict
from pandas.testing import assert_frame_equal


class TestLoaders(unittest.TestCase):
    def test_dict_to_df(self):
        input_dict = {'first': 3, 'second': 4}
        key_name = 'a'
        val_name = 'b'
        real_output = pd.DataFrame(data={'a': ['first', 'second'], 'b': [3, 4]})
        assert_frame_equal(real_output, dict_to_df(input_dict, key_name, val_name))

    def test_increment_count(self):
        test = {'a': 1}
        test = increment_count(test, 'a')
        self.assertEqual(test, {'a': 2})
        test = increment_count(test, 'b')
        self.assertEqual(test, {'a': 2, 'b': 1})

    def test_init_zero_dict(self):
        test = ['a', 'b', 'c']
        self.assertEqual(init_zero_dict(test), {'a': 0, 'b': 0, 'c': 0})


if __name__ == '__main__':
    unittest.main()
