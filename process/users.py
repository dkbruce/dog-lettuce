import pandas as pd

from loaders.loaders import DATA_PATH, load_file
from osu_requests.request_api import get_username
from process.helpers import dict_to_df


def get_all_usernames(verbose: bool = False) -> dict:
    user_path = DATA_PATH / 'users.txt'
    cache_path = DATA_PATH / 'users_cache.csv'
    user_ids = load_file(user_path)

    # load a cache csv of users in the server
    try:
        user_cache = pd.read_csv(cache_path)
        user_cache['user_id'] = user_cache['user_id'].astype(str)
        user_cache_ids = user_cache['user_id'].values
        id_to_username = pd.Series(user_cache['username'].values, index=user_cache['user_id']).to_dict()
    except:  # Cache doesn't exist
        user_cache = pd.DataFrame()
        user_cache_ids = []
        id_to_username = {}

    for user in user_ids:
        if user not in user_cache_ids:
            id_to_username[user] = get_username(user, verbose=verbose)

    dict_to_df(id_to_username, 'user_id', 'username').to_csv(cache_path)
    return id_to_username
