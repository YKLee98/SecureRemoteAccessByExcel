# logs/logger.py
import logging
import os
from datetime import datetime

LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
LOG_FILE = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log")

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("RemoteControlLogger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(file_handler)

def info(msg): logger.info(msg)
def warn(msg): logger.warning(msg)
def error(msg): logger.error(msg)
def debug(msg): logger.debug(msg)
