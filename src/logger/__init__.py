# Making Logging File
import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

# Constants for log configuration
LOG_DIR = 'logs'                                                    # The folder where log files will be saved.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"    #  Creates a log file name based on the current date and time.
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB    Sets the maximum size of each log file to 5 MB. If the log file exceeds this size, it will rotate.
BACKUP_COUNT = 3  # Number of backup log files to keep

# Construct log file path
log_dir_path = os.path.join(from_root(), LOG_DIR) #  Combines the project root directory (from from_root()) with the LOG_DIR name to create the path for the logs folder.
os.makedirs(log_dir_path, exist_ok=True) # Creates the logs folder if it doesn't already exist.
log_file_path = os.path.join(log_dir_path, LOG_FILE) # Combines the log_dir_path with the log file name to create the full file path for the current log.

def configure_logger():
    """
    Configures logging with a rotating file handler and a console handler.
    """
    # Create a custom logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    # Define formatter
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # File handler with rotation
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Configure the logger
configure_logger()