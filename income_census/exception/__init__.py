import os
import sys






class IC_Exception(Exception):
    
    """
    error_message : it represent as object of Exception class, 
                    we will get exception details (Exception message).

    error_detail : it will tell us about which file and which line is error occured.
    
    """
    
    
    def __init__(self, error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message = IC_Exception.get_detailed_error_message(error_message=error_message,
                                                                    error_detail=error_detail)


    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str:
        """
        Static method without creating object we can access this function"""
        
        _,_ ,exec_tb=error_detail.exc_info()
        
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        
        error_message = f"""
        Error occured in script: 
        [ {file_name} ] at 
        try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}] 
        error message: [{error_message}]
        """
        
        return error_message
    
    def __str__(self):
        return self.error_message

    def __repr__(self):
        return IC_Exception.__name__.str()
    
    