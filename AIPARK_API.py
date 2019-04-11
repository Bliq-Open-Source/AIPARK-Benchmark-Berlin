"""
    Implementation of getOccupancyForParkingAreas method of AIPARK API
    for Python3
"""
import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class AIPARK_API(object):

    def __init__(self,apikey):
        self.apikey = apikey
        self.endpoint = "https://api.aipark.io:443/aipark/v1/"


    def getOccupancyForParkingAreas(self,request_list):
        """
        request_list has the form: [{"parkingAreaId": 3376765,"timestamp": 1476561575000}]
        """
        req = {"timeParkingAreaId": request_list}
        request_url = self.endpoint + "getOccupancyForParkingAreas"
        response = self._performWebRequest(req,request_url)
        try:
            prediction = int(response["occupancies"][0]["value"])
        except Exception as e:
            print("Fetching prediction for ParkingAreaId: " + str(request_list[0]["parkingAreaId"]) + " failed with error: " + str(e))
            prediction = 0
        return prediction

    def _performWebRequest(self,req, request_url):
        response = None
        try:
            head = {"Content-Type":"application/json;charset=UTF-8","apikey":self.apikey}
            r = requests.post(request_url,json=req,headers=head,verify=False)
            try:
                response = r.json()
            except:
                response = r.status_code
                print("Webservice response code: " + str(response) + " for url: " + request_url)
        except Exception as e:
            print("API request failed with error: " + str(e))
        return response

if __name__ == "__main__":
    api = AIPARK_API(apikey="insert-your-api-key-here")
