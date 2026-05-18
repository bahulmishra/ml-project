# logger.py is used to create a logger object that can be used throughout the project to log messages. This is useful for debugging and monitoring the progress of our machine learning pipeline. We can configure the logger to log messages to a file or to the console, and we can set different logging levels (e.g., DEBUG, INFO, WARNING, ERROR) to control the verbosity of the logs. By using a logger, we can keep track of important events and errors in our code, which can help us identify and fix issues more efficiently.


import logging 
import os
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"                                            # we are creating a log file with the current date and time to store our log messages.
logs_path=os.path.join(os.getcwd(), "logs", LOG_FILE)                                                       # we are creating a path to the log file by joining the current working directory with the logs folder and the log file we just created.
os.makedirs(logs_path, exist_ok=True)                                                                       # we are creating the logs folder if it doesn't exist already.   
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)                                                           # we are creating the full path to the log file by joining the logs path with the log file name. 

logging.basicConfig(
    filename=LOG_FILE_PATH,                                                                                 # we are specifying the file where the log messages will be stored.
    format="[%(asctime)s %(lineno)d] %(name)s - %(levelname)s - %(message)s",                               # we are specifying the format of the log messages to include the timestamp, line number, logger name, log level, and the log message itself.
    level=logging.INFO,                                                                                     # we are setting the logging level to INFO, which means that only messages with a level of INFO or higher will be logged.
)

if __name__ == "__main__":
    logging.info("Logging has started.")                                                   # we are logging an INFO message to indicate that the logging has been configured successfully. This is just a test message to verify that our logger is working correctly.




