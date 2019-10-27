import requests

import pandas as pd

from config import api_key
from loaders.loaders import load_file
from pathlib import Path


def get_users():
    users = load_file()
