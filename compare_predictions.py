"""
    A simple script for comparing comparing ground truth data to
    parking availability data by AIPARK

    To use, you will need to sign up and create a free AIPARK studio account
    Sign up here: https://studio.aipark.io/sign-up/

    This script does
    1) Read data from ground_truth.csv
    2) Request predictions and capacity from AIPARK's On-Street API
    3) Calculate the accuracy as the number of correct predictions per total
    number of parking areas

    Python 3
"""

# libraries
import csv
import time
from datetime import datetime
from prediction_utilities import compare
from ParkingArea import ParkingArea
from AIPARK_API import AIPARK_API

def parse(filename):
    print("Parsing ground truth data...")
    data = []
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        for _, line in enumerate(reader):
            parking_area_id = int(line[0])
            timestamp = convert_timestring_to_unix(line[1])
            capacity = int(line[2])
            number_open_spots = int(line[3])
            data.append(ParkingArea(parking_area_id, timestamp, capacity, number_open_spots))
    return data

def convert_timestring_to_unix(timestring):
    d = datetime.strptime(timestring, '%Y-%m-%d %H:%M:%S.%f')
    unixtime = int(time.mktime(d.timetuple()))*1000
    return unixtime

def request_predictions(parking_areas):
    print("Fetching predictive parking data...")
    for p_area in parking_areas:
        prediction = api.getOccupancyForParkingAreas([{"parkingAreaId": p_area.parking_area_id,"timestamp": p_area.timestamp}])
        p_area.set_prediction(prediction)
        time.sleep(0.1)

def compute_statistics(parking_areas):
    total = len(parking_areas)
    true_counter = 0
    print("")
    print("Results - Description of errors:")
    print("")
    for p_area in parking_areas:
        if compare(p_area.get_prediction(),p_area.get_occupancy()):
            true_counter += 1
        else:
            print("ParkingAreaId " + str(p_area.parking_area_id) + " result: false, prediction: " +
            p_area.get_discrete_prediction() + ", occupancy: " + str(float("{0:.2f}".format(p_area.get_occupancy()))) + ", capacity: " + str(p_area.capacity))

    print("")
    print("#total parking areas: " + str(total) + " | #correct predictions: " + str(true_counter) +
    " | correct predictions [%]: " + str(float("{0:.2f}".format(100*float(true_counter)/float(total)))) + "%")



def run_comparison():
    # 1) parse input data
    parking_areas = parse("ground_truth.csv")

    # 2) request predictions
    request_predictions(parking_areas)

    # 3) compute statistics
    compute_statistics(parking_areas)


if __name__ == "__main__":
    api = AIPARK_API(apikey="insert-your-api-key-here")
    run_comparison()
