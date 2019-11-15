import datetime
import os
import sqlalchemy

import pandas as pd

from osu_requests.request_api import get_top_scores, create_beatmap_info_csv
from loaders.loaders import load_file, DATA_PATH
from process.helpers import dict_to_df, increment_count, init_zero_dict, init_empty_list_dict
from process.users import get_all_usernames


def count_top_scores(beatmap_file: str, aggregation_function, score_limit: int = 50, verbose: bool = False,
                     to_csv: bool = False) -> pd.DataFrame:
    users = load_file(DATA_PATH / 'users.txt')
    beatmaps = load_file(DATA_PATH / 'challenges' / beatmap_file)
    table_name = beatmap_file.split('.')[0]

    try:
        map_info = pd.read_csv(DATA_PATH / 'map_info' / (beatmap_file.split('.')[0] + '.csv'), index_col=0)
    except:
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

    current_time = datetime.datetime.utcnow().isoformat()

    output_df['time'] = current_time

    if to_csv:
        output_df.to_csv(DATA_PATH / 'results' / (beatmap_file.split('.')[0] + 'results.csv'))

    # DATABASE_URL = os.environ['DATABASE_URL']
    DATABASE_URL = 'postgres://sagbwsnabpfjez:53d57f42dc9b468afc4788e73fb880f4403f08392b3ed62f3e37a990b3442f8d@ec2-107-20-198-176.compute-1.amazonaws.com:5432/dr0pq5hvd3e29'
    conn = sqlalchemy.create_engine(DATABASE_URL)
    c = conn.connect()
    trans = c.begin()
    try:
        c.execute(f'''DROP TABLE IF EXISTS {table_name}''')
        trans.commit()
    except:
        trans.rollback()
        raise
    output_df.to_sql(f'{table_name}', conn)
    c.close()

    return output_df
