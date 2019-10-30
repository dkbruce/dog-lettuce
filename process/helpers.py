import os
import sqlalchemy
import pandas as pd


def dict_to_df(input_dict: dict, key_name: str, val_name: str) -> pd.DataFrame:
    out = pd.Series(input_dict, name=val_name)
    out.index.name = key_name
    return out.reset_index()


def init_zero_dict(input_list: list) -> dict:
    output_dict = {}
    for item in input_list:
        output_dict[item] = 0
    return output_dict


def init_empty_list_dict(input_list: list) -> dict:
    output_dict = {}
    for item in input_list:
        output_dict[item] = []
    return output_dict


def increment_count(user_count: dict, user_id: str):
    if user_id in user_count:
        user_count[user_id] += 1
    else:
        user_count[user_id] = 1
    return user_count


def most_recent_time():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = sqlalchemy.create_engine(DATABASE_URL)
    c = conn.connect()
    try:
        row = c.execute('''SELECT * FROM Time''')
    except:
        row = [None]
    finally:
        c.close()
        return row[0]


