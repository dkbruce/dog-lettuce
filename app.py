import os

import pandas as pd

api_key = os.environ['API_KEY']

from flask import Flask, render_template
from loaders.loaders import DATA_PATH, load_last_update

from process.top_scores import count_top_scores
from process.aggregation import challenge0001_agg

from main import beatmaps_file

app = Flask(__name__)


@app.route("/")
def home():
    scores_df = pd.read_csv(DATA_PATH / 'results' / 'challenge0001results.csv', index_col=0).drop(columns='maps_played')
    last_update = load_last_update()
    return render_template('home.html', column_names=scores_df.columns.values, row_data=list(scores_df.values.tolist()),
                           last_update=last_update, zip=zip)


if __name__ == "__main__":
    print('hi')
    count_top_scores(beatmaps_file, challenge0001_agg, 8, verbose=True, to_csv=True)
    app.run()
