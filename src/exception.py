# exception.py is a file that contains custom exception classes that we can use in our machine learning project. These custom exceptions can help us handle specific error cases in a more organized and meaningful way. For example, we might create a custom exception for data validation errors, model training errors, or any other specific issues that we anticipate encountering in our project. By using custom exceptions, we can provide more informative error messages and make it easier to debug and maintain our code.

# sys module provides various functions and variables that are used to manipulate different parts of the Python runtime environment. In the context of exception handling, we can use the sys module to access information about the current exception being handled, such as the exception type, value, and traceback. This can be useful for logging error details or for re-raising exceptions with additional context. For example, we can use sys.exc_info() to get information about the current exception and then log that information or include it in a custom error message when raising a new exception.

import sys

def error_message_details(error, error_detail: sys):                                       # whenever a exception occurs we are going to call this function and pass the error and the sys module to it, and it will return a string with the error message details.
    _,_,exe_tb = error_detail.exc_info()                                                   # exc_info() returns a tuple of three values: (type, value, traceback). We are only interested in the traceback, so we unpack the tuple and ignore the first two values.
    file_name = exe_tb.tb_frame.f_code.co_filename 
    error_message = "Error occurred in script: [{0}] at line number: [{1}] error message: [{2}]".format(
        file_name, exe_tb.tb_lineno,str(error)
        
        return error_message

        )                                                                                  # we are going to format the error message to include the filename, line number, and the error message itself.
    
class CustomException(Exception):                                                          # we are creating a custom exception class that inherits from the built-in Exception class.
    def __init__(self, error_message, error_detail: sys):                                  # the constructor takes in an error message and the sys module as parameters.
        super().__init__(error_message)                                                    # we call the constructor of the parent class (Exception) to initialize the error message.
        self.error_message = error_message_details(error_message, error_detail)            # we call the error_message_details function to get the detailed error message and assign it to an instance variable.

    def __str__(self):                                                                     # we override the __str__ method to return the detailed error message when the exception is printed.
        return self.error_message
    





