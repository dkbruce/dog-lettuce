from process.top_scores import count_top_scores
from process.aggregation import challenge0001_agg

if __name__ == '__main__':
    beatmaps = 'challenge0001.txt'

    user_count = count_top_scores(beatmaps, challenge0001_agg, 8, verbose=True, to_csv=True)
