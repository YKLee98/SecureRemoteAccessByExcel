# src/server/logger.py
import logging
from datetime import datetime
import os

LOG_DIR = "logs"

def init_logger():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(
        filename=os.path.join(LOG_DIR, f"{datetime.now().date()}_server.log"),
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

def log_event(addr, msg):
    logging.info(f"{addr} - {msg}")
