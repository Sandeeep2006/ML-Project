import sys 
import logging
import logger

def error_messsage_details(error,error_details:sys):
    _,_,exe_tb=error_details.exc_info()   #stores the info about the exception
    file_name=exe_tb.tb_frame.f_code.co_filename
    error_msg="Error occured in Python Script name[{0}], line number [{1}], error message [{2}]".format(
        file_name,exe_tb.tb_frame.f_lineno,str(error)
    )
    return error_msg
    
class CustomException(Exception):
    def __init__(self,error_message,details:sys):
        super().__init__(error_message)
        self.error_message=error_messsage_details(error_message,error_details=details)
        
    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logger.logging.info("Division by Zero Errorawdaw.")
        raise CustomException(e,sys)