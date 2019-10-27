from process.top_scores import count_top_scores
from process.users import get_all_usernames

if __name__ == '__main__':
    beatmaps = 'challenge0001.txt'

    user_count = count_top_scores(beatmaps, 8, verbose=True, to_csv=True)
