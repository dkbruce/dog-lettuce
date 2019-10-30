import os
import sqlalchemy

import pandas as pd

api_key = os.environ['API_KEY']

from flask import Flask, render_template
from loaders.loaders import DATA_PATH, load_last_update

from process.top_scores import count_top_scores
from process.aggregation import challenge0001_agg
from process.helpers import most_recent_time

from main import beatmaps_file

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']
conn = sqlalchemy.create_engine(DATABASE_URL)
c = conn.connect()


@app.route("/")
def home():
    query = c.execute("SELECT user_id, challenge_score, username FROM competition0001")
    scores_df = pd.DataFrame(query.fetchall())
    scores_df.columns = query.keys()
    return render_template('home.html', column_names=scores_df.columns.values, row_data=list(scores_df.values.tolist())
                           , zip=zip)


if __name__ == "__main__":
    count_top_scores(beatmaps_file, challenge0001_agg, 8, verbose=True, to_csv=False)
    app.run()
