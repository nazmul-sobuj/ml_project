import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    
    if exc_tb is not None:
        filename = exc_tb.tb_frame.f_code.co_filename
        error_message = "Error occurred in the script [{0}] at line [{1}]: {2}".format(
            filename, exc_tb.tb_lineno, str(error)
        )
    else:
        error_message = f"Error occurred: {str(error)}"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_detail(error_message, error_detail)
        logging.error(self.error_message)  # Optional: log when error is created
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message

    







   