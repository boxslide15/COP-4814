import json
import requests
from json2xml import json2xml, readfromjson

def save_to_file(filename, data):
    with open(filename, "w") as write_file:
        json.dump(data, write_file, indent=4)
        print("The file {0} was successfully created.".format(filename))

def read_from_file(filename):
    with open(filename, "r") as read_file:
        jsonData = json.load(read_file)
        print("You have successfully read from {0}".format(filename))
        return jsonData

def save_xml_file(filename):
    with open(filename, "w") as write_file:
        xmlHeader = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"aqi.xsl\"?>\n"
        data = readfromjson("aqi.json")
        aqi_xml = json2xml.Json2xml(data).to_xml()
        write_file.write(xmlHeader)
        write_file.write(aqi_xml)
        print("The file {0} was successfully created.".format(filename))

def apiRequest():
    api_key = read_from_file("api_key.json")
    my_aqi_api_key = api_key["aqi_api_key"]
    url = "http://api.airvisual.com/v2/nearest_city?key="
    url = url + my_aqi_api_key
    aqi_json_file_name = "aqi.json"
    json_file = requests.get(url).json()
    save_to_file(aqi_json_file_name, json_file)

apiRequest()

save_xml_file("aqi.xml")