from datetime import date

def programNine(month, day, year):
    calculatedTime = 10**9

    yourBirthday = date(year, month, day)

    return yourBirthday + calculatedTime

month = int(input("Please enter your birth month MM: "))

day = int(input("Please enter your birth day DD: "))

year = int(input("Please enter your birth year YYYY: "))

print(programNine(month, day, year))

    


    

