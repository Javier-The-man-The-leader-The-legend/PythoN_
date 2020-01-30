import requests
from math import floor
header_data ={"cookie":
"session=53616c7465645f5f09ea9e523bddc1ab2d7b14d71aeb8ec207dec6ede50f3987246940e8fb4e660b88b0e30ff8e49937"
}
r = requests.get("https://adventofcode.com/2019/day/1/input", headers=header_data)
if r.status_code == 200:
    a = r.text.splitlines()
masses = [int(s) for s in a]
def calculate_fuel(mass):
    return floor(mass / 3) - 2
fuel = 0
fuell = 0 
for mass in masses:
    print("Calculating module {}".format(mass))
    fuel += calculate_fuel(mass)
    fuuel = calculate_fuel(mass)
    while fuuel >= 0:
        fuuel = calculate_fuel(fuuel)
        print("adding fuel {}".format(fuuel))
        fuell += fuuel
    fuell -= fuuel
answersofanswersofansewrs = fuel + fuell
print(answersofanswersofansewrs)