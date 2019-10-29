import os

import pandas as pd

from flask import Flask, render_template
from loaders.loaders import DATA_PATH, load_last_update

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route("/")
def home():
    scores_df = pd.read_csv(DATA_PATH / 'results' / 'challenge0001results.csv', index_col=0).drop(columns='maps_played')
    last_update = load_last_update()
    return render_template('home.html', column_names=scores_df.columns.values, row_data=list(scores_df.values.tolist()),
                           last_update=last_update, zip=zip)


if __name__ == "__main__":
    print(os.environ['APP_SETTINGS'])
    app.run()
