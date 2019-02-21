import json
import requests

def save_to_file(filename, data):
    with open(filename, "w") as write_file:
        json.dump(data, write_file, indent=4)
        print("The file {0} was successfully created.".format(filename))

def read_from_file(filename):
    with open(filename, "r") as read_file:
        jsonData = json.load(read_file)
        print("You have successfully read from {0}".format(filename))
        return jsonData

api_key = read_from_file("api_key.json")

my_aqi_api_key = api_key["aqi_api_key"]

url = "http://api.airvisual.com/v2/nearest_city?key="

url = url + my_aqi_api_key

aqi_json_file_name = "aqi.json"

json_file = requests.get(url).json()

save_to_file(aqi_json_file_name, json_file)

air_quality_index = read_from_file(aqi_json_file_name)

longitude = air_quality_index["data"]["location"]["coordinates"][0]

latitude = air_quality_index["data"]["location"]["coordinates"][1]

print(latitude)
print(longitude)