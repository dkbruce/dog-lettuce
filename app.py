import os
import psycopg2

import pandas as pd

api_key = os.environ['API_KEY']

from flask import Flask, render_template
from loaders.loaders import DATA_PATH, load_last_update

from process.top_scores import count_top_scores
from process.aggregation import challenge0001_agg

from main import beatmaps_file

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
c = conn.cursor()


@app.route("/")
def home():
    query = c.execute("SELECT * FROM competition0001")
    scores_df = pd.DataFrame(query.fetchall())
    scores_df.columns = query.keys()
    last_update = load_last_update()
    return render_template('home.html', column_names=scores_df.columns.values, row_data=list(scores_df.values.tolist()),
                           last_update=last_update, zip=zip)


if __name__ == "__main__":
    print('hi')
    count_top_scores(beatmaps_file, challenge0001_agg, 8, verbose=True, to_csv=True)
    app.run()
