from datetime import datetime
import logging
import os

class Logger:
    def __init__(self, run_id, log_module, log_file_name):
        self.logger = logging.getLogger(f"{log_module}_{run_id}")
        self.logger.setLevel(logging.DEBUG)

        # Set up the log file path based on log_file_name
        if log_file_name == 'training':
            log_dir = 'C:\\Users\\patel\\Desktop\\Projects2\\endtoend-ml-projects-master\\EndtoEndML_v11\\logs\\training_logs'
            log_file = os.path.join(log_dir, f'train_log_{run_id}.log')
        else:
            log_dir = 'C:\\Users\\patel\\Desktop\\Projects2\\endtoend-ml-projects-master\\EndtoEndML_v11\\logs\\prediction_logs'
            log_file = os.path.join(log_dir, f'predict_log_{run_id}.log')

        # Create a file handler
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        self.logger.addHandler(file_handler)

    def info(self, message):
        self.logger.info(message)

    def exception(self, message):
        self.logger.exception(message)
