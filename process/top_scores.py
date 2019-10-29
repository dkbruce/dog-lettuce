import datetime

import pandas as pd

from osu_requests.request_api import get_top_scores, create_beatmap_info_csv
from loaders.loaders import load_file, DATA_PATH
from process.helpers import dict_to_df, increment_count, init_zero_dict, init_empty_list_dict
from process.users import get_all_usernames


def count_top_scores(beatmap_file: str, aggregation_function, score_limit: int = 50, verbose: bool = False,
                     to_csv: bool = True) -> pd.DataFrame:
    users = load_file(DATA_PATH / 'users.txt')
    beatmaps = load_file(DATA_PATH / 'challenges' / beatmap_file)

    try:
        map_info = pd.read_csv(DATA_PATH / 'map_info' / (beatmap_file.split('.')[0] + '.csv'), index_col=0)
    except FileNotFoundError:
        create_beatmap_info_csv(beatmap_file, verbose=verbose)
        map_info = pd.read_csv(DATA_PATH / 'map_info' / (beatmap_file.split('.')[0] + '.csv'), index_col=0)

    map_list = []
    challenge_score = init_zero_dict(users)
    user_maps = init_empty_list_dict(users)
    for beatmap in beatmaps:
        map_list.append(get_top_scores(beatmap, score_limit, verbose))

    for beatmap, beatmap_id in zip(map_list, beatmaps):
        for play in beatmap:
            user_id = play['user_id']
            if user_id in users:
                challenge_score[user_id] += aggregation_function(map_info[map_info['beatmap_id']
                                                                          == int(beatmap_id)].squeeze())
                user_maps[user_id].append(beatmap_id)

    for user in users:
        if user not in challenge_score.keys():
            challenge_score[user] = 0
        challenge_score[user] = round(challenge_score[user], 2)

    output_df = dict_to_df(challenge_score, 'user_id', 'challenge_score')\
        .sort_values(by='challenge_score', ascending=False)
    output_df['username'] = output_df['user_id'].map(get_all_usernames(verbose=verbose))
    output_df['maps_played'] = output_df['user_id'].map(user_maps)
    if to_csv:
        output_df.to_csv(DATA_PATH / 'results' / (beatmap_file.split('.')[0] + 'results.csv'))

    current_time = datetime.datetime.utcnow().isoformat()

    with open(DATA_PATH / 'last_update.txt', 'w') as f:
        f.write(current_time)

    return output_df
