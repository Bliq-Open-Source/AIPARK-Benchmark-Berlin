"""
    Utilities for comparing predictive parking data with ground truth values
    Python 3
"""

# libraries
import numpy as np

def discretize_prediction(prediction):
    if inRange(prediction,0,34):
        return "low"
    elif inRange(prediction,34,67):
        return "high"
    elif inRange(prediction,67,100):
        return "very high"
    else:
        raise ValueError("Input value " + str(prediction) + " out of range.")

def inRange(value,lower_bound,upper_bound):
    if lower_bound <= value <= upper_bound:
        return True
    else:
        return False


def compare(prediction, actual_value):
    """
    prediction is a value between 0 and 100
    actual_value is the number of open spots / total capacity
    return value states, if the prediction was true or false
    """
    d = discretize_prediction(prediction)
    if inRange(actual_value,0,1/3) and d is "low":
        return True
    elif inRange(actual_value,1/3,2/3) and d is "high":
        return True
    elif inRange(actual_value,2/3,1) and d is "very_high":
        return True
    else:
        return False

if __name__ == "__main__":
    pass
