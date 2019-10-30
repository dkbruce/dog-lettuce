from process.top_scores import count_top_scores
from process.aggregation import challenge0001_agg

beatmaps_file = 'challenge0001.txt'

if __name__ == '__main__':
    user_count = count_top_scores(beatmaps_file, challenge0001_agg, 8, verbose=True, to_csv=True)
    with open('data/last_update', 'r') as f:
        lines = f.readlines()
    print(lines)