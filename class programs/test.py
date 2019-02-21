class Starship(object):
    sound = 'Vrrrrrrrr'
    
    def __init__(self):
        self.engines = False
        self.engine_speed = 0
        self.shield = True
    
    def engage(self):
        self.engines = True
    
    def warp(self, factor):
        self.engine_speed = 2
        self.engine_speed *= factor

enterprise_ = Starship()

enterprise_.warp(4)
enterprise_.engage()
print(enterprise_.engines)
print(enterprise_.engine_speed)

class Elf():
    def __init__(self, level, ability_scores = None):
        self.level = level
        self.ability_scores = {
            "str" : 11, "dex" : 12, "con" : 10, "int" : 16, "wis" : 14, "cha" : 13
        } if ability_scores == None else ability_scores
        self.hp = 20 + self.ability_scores["cha"]

gregElf = Elf("first_level", {
    "str" : 15, "dex" : 9, "con" : 10, "int" : 10, "wis" : 12, "cha" : 15
    })

bobElf = Elf("second_level")

print(gregElf.hp)

print(bobElf.hp)

release_date = {"iphone" : 2007, 
                "iphone 4" : 2010,
                "iphone 5s" : 2013,
                "iphone 7" : 2016,
                "iphone x" : 2017}

print(release_date)

release_date["iphone xr"] = 2018

print(release_date)

del release_date["iphone"]

print(release_date)

for i,j in release_date.items():
    print(i,j)

Capitals = dict()

Capitals['USA'] = "Washington DC"
Capitals['Jordan'] = "Amman"
Capitals['France'] = "Paris"
Capitals['UK'] = "London"
Capitals['Brazil'] = "Brasilia"

print(Capitals)

Countries = ['France', 'Lebanon', 'USA', 'Brazil', 'Colombia']

for i in Countries:
    if i in Capitals:
        print("The capital of " + i + " is: " + Capitals[i])
    else:
        print("Unknown capital")

def factorial(x):
    fact = 1
    for i in range (1, x + 1):
        fact *= i
    return fact

def factorial2(x):
    if x < 1:
        return 1
    else:
        return x * factorial2((x - 1))

print(factorial(8))

print(factorial2(8))

def max_(x, y):
    if x > y:
        return x
    else:
        return y

print(max_(int(input()), int(input())))