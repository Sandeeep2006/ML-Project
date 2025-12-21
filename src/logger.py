import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d %H_%M_%S')}.log"      #creating a log file FILE NAME
logs_path=os.path.join(os.getcwd(),"logs")  # gets the current working directory and puts the log file there
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ]| line:%(lineno)d | %(name)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)

# if __name__=="__main__":
#     logging.info("Logging has started")