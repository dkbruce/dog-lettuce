import pandas as pd


def competition0001_agg(info: pd.Series) -> float:
    if info['difficultyrating'] < 2.0:
        return 0.4
    if info['difficultyrating'] < 2.7:
        return 0.65
    return 1

def competition0002_agg(info: pd.Series) -> float:
    if info['difficultyrating'] < 2.0:
        return 0.4
    if info['difficultyrating'] < 2.7:
        return 0.65
    return 1
