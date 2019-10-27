import pandas as pd


def dict_to_df(input_dict: dict, key_name: str, val_name: str) -> pd.DataFrame:
    out = pd.Series(input_dict, name=val_name)
    out.index.name = key_name
    return out.reset_index()


def increment_count(user_count: dict, user_id: str):
    if user_id in user_count:
        user_count[user_id] += 1
    else:
        user_count[user_id] = 1
    return user_count