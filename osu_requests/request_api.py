import requests

from time import sleep
from config import api_key

API_BASE = 'https://osu.ppy.sh/api/'


def get_top_scores(beatmap: str, num_scores: int = 50, verbose: bool = False, sleep_time: float = 0.1) -> list:
    params = {
        'k': api_key,
        'b': beatmap,
        'limit': num_scores
    }
    endpoint = 'get_scores'
    if verbose:
        print(f'Querying beatmap: {beatmap}')
    req = req_osu_api(endpoint=endpoint, params=params, sleep_time=sleep_time)
    if req.status_code != 200:
        print('Status not 200')
        return []
    return req.json()


def get_username(user_id: str, verbose: bool = False, sleep_time: float = 0.1) -> str:
    params = {
        'k': api_key,
        'u': user_id,
        'type': 'u'
    }
    endpoint = 'get_user'
    if verbose:
        print(f'Querying user: {user_id}')
    req = req_osu_api(endpoint=endpoint, params=params, sleep_time=sleep_time)
    if req.status_code != 200:
        print('Status not 200')
        return ''
    return req.json()[0]['username']


def req_osu_api(endpoint: str, params: dict, sleep_time: float) -> requests.models.Response:
    output = requests.get(API_BASE + endpoint, params)
    sleep(sleep_time)
    return output
