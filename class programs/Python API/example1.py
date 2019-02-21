import json
import main_functions
import requests

print("Example 1 - How many astronauts are in space right now")

url = "http://api.open-notify.org/astros.json"

astronauts_json = requests.get(url).json()

#main_functions.save_to_file("astronauts.json", astronauts_json)
astronauts_in_space = main_functions.read_from_file("astronauts.json")

for i in astronauts_in_space['people']:
    print(i['name'])