import curses
import textwrap
import threading
import time
import itertools
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("make .env file with API_KEY=your_key")
SERVER_URL = "https://ai.hackclub.com/proxy/v1"

