"""
    Simple Parking Area Object Class
"""
from prediction_utilities import discretize_prediction

class ParkingArea(object):

    def __init__(self,parking_area_id, timestamp, capacity, number_open_spots):
        self.parking_area_id = parking_area_id
        self.timestamp = timestamp
        self.capacity = capacity
        self.number_open_spots = number_open_spots

    def set_prediction(self,prediction):
        self.prediction = prediction

    def get_occupancy(self):
        return float(self.number_open_spots) / float(self.capacity)

    def get_prediction(self):
        return self.prediction

    def get_discrete_prediction(self):
        return discretize_prediction(self.prediction)
