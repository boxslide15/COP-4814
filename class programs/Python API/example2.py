import json
import main_functions
import requests

print("Mars Rover Photos API: \n")

api_key = main_functions.read_from_file("nasa_api.json")

my_api_key = api_key["APIKey"]

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key="

url2 = url + my_api_key

#mars_pics = requests.get(url2).json()

#main_functions.save_to_file("mars_pics.json", mars_pics)

mars_pics = main_functions.read_from_file("mars_pics.json")

print(type(mars_pics))

print(mars_pics["photos"][0].keys())

for i in mars_pics["photos"]:
    if i["camera"]["name"] == "NAVCAM":
        print(i["img_src"])