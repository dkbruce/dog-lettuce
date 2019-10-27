import pandas as pd


def dict_to_df(input_dict: dict, key_name: str, val_name: str) -> pd.DataFrame:
    out = pd.Series(input_dict, name=val_name)
    out.index.name = key_name
    return out.reset_index()