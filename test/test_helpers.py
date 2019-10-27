import unittest

import pandas as pd

from process.helpers import dict_to_df
from pandas.testing import assert_frame_equal


class TestLoaders(unittest.TestCase):
    def test_dict_to_df(self):
        input_dict = {'first': 3, 'second': 4}
        key_name = 'a'
        val_name = 'b'
        real_output = pd.DataFrame(data={'a': ['first', 'second'], 'b': [3, 4]})
        assert_frame_equal(real_output, dict_to_df(input_dict, key_name, val_name))


if __name__ == '__main__':
    unittest.main()
