import os
import sys
import logging
from datetime import datetime
# file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#create directory
logs_path = os.path.join(os.getcwd(), "logs")

#create directory if not exist
os.makedirs(logs_path, exist_ok= True)

#full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# basic log configure
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


if __name__ == "__main__":
    logging.info("Logging has started")
