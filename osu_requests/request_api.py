import requests

import pandas as pd

from time import sleep
from apikey import api_key
from loaders.loaders import DATA_PATH, load_file

API_BASE = 'https://osu.ppy.sh/api/'


def create_beatmap_info_csv(beatmap_file: str, verbose: bool = False, sleep_time: float = 0.1):
    beatmap_list = []
    beatmaps = load_file(DATA_PATH / beatmap_file)
    for beatmap in beatmaps:
        beatmap_list.append(get_beatmap_info(beatmap, verbose, sleep_time=sleep_time))
    info_df = pd.DataFrame(beatmap_list)
    info_df.to_csv(DATA_PATH / 'map_info' / (beatmap_file.split('.')[0] + '.csv'))


def get_beatmap_info(beatmap: str, verbose: bool = False, sleep_time: float = 0.1) -> dict:
    params = {
        'k': api_key,
        'b': beatmap,
    }
    endpoint = 'get_beatmaps'
    req = setup_endpoint(endpoint, params, sleep_time, verbose)
    return req.json()


def get_top_scores(beatmap: str, num_scores: int = 50, verbose: bool = False, sleep_time: float = 0.1) -> list:
    params = {
        'k': api_key,
        'b': beatmap,
        'limit': num_scores
    }
    endpoint = 'get_scores'
    req = setup_endpoint(endpoint, params, sleep_time, verbose)
    return req.json()


def get_username(user_id: str, verbose: bool = False, sleep_time: float = 0.1) -> str:
    params = {
        'k': api_key,
        'u': user_id,
        'type': 'u'
    }
    endpoint = 'get_user'
    req = setup_endpoint(endpoint, params, sleep_time, verbose)
    return req.json()[0]['username']


def setup_endpoint(endpoint: str, params: dict, sleep_time: float, verbose: bool = False):
    if verbose:
        print(f'Querying endpoint: {endpoint}')
        print(f'Querying params: {params}')
    req = req_osu_api(endpoint=endpoint, params=params, sleep_time=sleep_time)
    if req.status_code != 200:
        print('Status not 200')
        raise Exception
    return req


def req_osu_api(endpoint: str, params: dict, sleep_time: float) -> requests.models.Response:
    output = requests.get(API_BASE + endpoint, params)
    sleep(sleep_time)
    return output
