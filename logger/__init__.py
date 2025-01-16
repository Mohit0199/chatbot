import logging
from datetime import datetime
import os

class CustomLogger:
    """Custom Logger class for Application"""

    def __init__(self):
        self.log_dir = 'logs'
        os.makedirs(self.log_dir, exist_ok=True)

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        log_file = os.path.join(self.log_dir, f"app_{timestamp}.log")

        logging.basicConfig(
            filename=log_file,
            filemode='w',
            format="[%(asctime)s] %(levelname)s - %(message)s",
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)


    def get_logger(self):
        """Returns the config logger"""
        return self.logger
