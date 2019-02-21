import json

with open("./sch.json", "r") as read_file:
    sch = json.load(read_file)

for i in sch["members"]:
    print("{0} has a strength of {1}".format(i["name"], i["strength"]))

x = lambda a, b : a * b

print(x(4,5))