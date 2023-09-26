import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" # it will print logging history in the format of time directory module and message

log_dir = "logs" # directory of log 
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True) # it will create logs directory

logging.basicConfig(
    level=logging.INFO, # it will retrive log information
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) # it prints output log in the console screen
    ]
)

logger = logging.getLogger("Cat-Or-Dog-Classification-logger") # naming the log 