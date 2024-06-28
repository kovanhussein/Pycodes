import logging

class CustomError(Exception):
    pass

def process_data(data):
    if data <= 0:
        raise CustomError("Data must be positive")
    return data
