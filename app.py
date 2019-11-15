import os
import sqlalchemy

import pandas as pd

from pathlib import Path
from flask import Flask, render_template
from loaders.loaders import DATA_PATH, load_file

DATABASE_URL = os.environ['DATABASE_URL']

app = Flask(__name__)

CURRENT_COMPETITION = 'competition0002'


@app.route("/")
def home():
    conn = sqlalchemy.create_engine(DATABASE_URL)
    c = conn.connect()
    trans = c.begin()
    try:
        query = c.execute(f"SELECT user_id, challenge_score, username, time, maps_played FROM {CURRENT_COMPETITION}")
        scores_df = pd.DataFrame(query.fetchall())
        scores_df.columns = query.keys()
        time = scores_df['time'].iloc[0]
        scores_df = scores_df[['username', 'user_id', 'challenge_score', 'username', 'maps_played']]
        visible_cols = ['username', 'user_id', 'challenge_score']
        trans.commit()
    except:
        trans.rollback()
        raise
    c.close()
    info = load_file(DATA_PATH / 'challenge_info' / f'{CURRENT_COMPETITION}.txt')
    title = info[0]
    info = info[1:]
    return render_template('home.html', column_names=visible_cols, row_data=list(scores_df.values.tolist()),
                           last_update=time, title=title, info=info, zip=zip)


@app.route("/history")
def history():
    tables = ['competition0001']
    conn = sqlalchemy.create_engine(DATABASE_URL)
    c = conn.connect()
    trans = c.begin()
    try:
        query = c.execute("SELECT user_id, challenge_score, username, time, maps_played FROM competition0001")
        scores_df = pd.DataFrame(query.fetchall())
        scores_df.columns = query.keys()
        time = scores_df['time'].iloc[0]
        scores_df = scores_df[['username', 'user_id', 'challenge_score', 'username', 'maps_played']]
        visible_cols = ['username', 'user_id', 'challenge_score']
        trans.commit()
    except:
        trans.rollback()
        raise
    c.close()
    info = load_file(DATA_PATH / 'challenge_info' / 'competition0001.txt')
    title = info[0]
    info = info[1:]
    return render_template('history.html', column_names=visible_cols, row_data=list(scores_df.values.tolist()),
                           last_update=time, title=title, info=info, tables=tables, zip=zip, enumerate=enumerate)


if __name__ == "__main__":
    app.run()
