import schedule
import time

from process.top_scores import count_top_scores
from process.aggregation import challenge0001_agg
from main import beatmaps_file


def run_query():
    count_top_scores(beatmaps_file, challenge0001_agg, 8, verbose=True, to_csv=True)


if __name__ == '__main__':
    while True:
        schedule.every().hour.do()
        time.sleep(1)