import os

from process.top_scores import count_top_scores
from process.aggregation import *

from app import CURRENT_COMPETITION

beatmaps_file = f'{CURRENT_COMPETITION}.txt'

if __name__ == '__main__':
    user_count = count_top_scores(beatmaps_file, competition0002_agg, 8, verbose=True)