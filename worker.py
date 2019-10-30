import schedule
import time

from process.top_scores import count_top_scores
from process.aggregation import challenge0001_agg
from main import beatmaps_file


def run_query():
    count_top_scores(beatmaps_file, challenge0001_agg, 8, verbose=True, to_csv=True)


def test_print():
    print('hi')


if __name__ == '__main__':
    test_print()
    while True:
        schedule.every().second.do(test_print)
        time.sleep(1)
