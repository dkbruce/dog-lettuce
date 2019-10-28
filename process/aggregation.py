import pandas as pd


def challenge0001_agg(info: pd.Series) -> float:
    if info['difficultyrating'] < 2.0:
        return 0.4
    elif info['difficultyrating'] < 2.7:
        return 0.65
    else:
        return 1
