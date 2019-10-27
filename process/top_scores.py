from osu_requests.request_api import get_top_scores
from loaders.loaders import load_file, DATA_PATH
from process.helpers import dict_to_df
from process.users import get_all_usernames


def count_top_scores(beatmap_file: str, score_limit: int = 50, verbose: bool = False, to_csv: bool = True) -> dict:
    users = load_file(DATA_PATH / 'users.txt')
    beatmaps = load_file(DATA_PATH / beatmap_file)

    map_list = []
    user_count = {}
    for beatmap in beatmaps:
        map_list.append(get_top_scores(beatmap, score_limit, verbose))

    for beatmap in map_list:
        for play in beatmap:
            user_id = play['user_id']
            if user_id in users:
                user_count = increment_count(user_count, user_id)

    for user in users:
        if user not in user_count.keys():
            user_count[user] = 0

    output_df = dict_to_df(user_count, 'user_id', 'leaderboard_count')
    output_df['username'] = output_df['user_id'].map(get_all_usernames(verbose=verbose))
    if to_csv:
        output_df.to_csv(DATA_PATH / (beatmap_file.split('.')[0] + '.csv'))

    return user_count


def increment_count(user_count: dict, user_id: str):
    if user_id in user_count:
        user_count[user_id] += 1
    else:
        user_count[user_id] = 1
    return user_count
