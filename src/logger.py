import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Generate log file name with timestamp
LOG_FILE = os.path.join(LOG_DIR, f"error_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Set up logging configuration
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,  # or logging.ERROR
    format='%(asctime)s - %(levelname)s - %(message)s',
)


if __name__ == "__main__":
    logging.info('Logging has started')