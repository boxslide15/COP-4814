import json

class Elf():
    def __init__(self, level, ability_scores = None):
        self.level = level
        self.ability_scores = {
            "str" : 11, "dex" : 12, "con" : 10, "int" : 16, "wis" : 14, "cha" : 13
        } if ability_scores == None else ability_scores
        self.hp = 20 + self.ability_scores["cha"]

myElf = Elf("First Level")

gregElf = Elf("Second Level", {"str" : 13, "dex" : 15, "con" : 9, "int" : 12, "wis" :10, "cha" : 8})

s = json.dumps(gregElf.__dict__)
j = json.dumps(myElf.__dict__)

t = json.loads(s)

with open('./elf_objects.json', 'w') as write_file:
    json.dump(t, write_file, indent=4)

print(t['ability_scores']['wis'])