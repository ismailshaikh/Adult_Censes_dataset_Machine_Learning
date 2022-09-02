import os
import sys
from tkinter import EXCEPTION

class AICException(Exception):

    def __init__(self, error_message: Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message =
    



    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str:
        pass


    def __str__(self):
        pass

    def __repr__(self):
        pass