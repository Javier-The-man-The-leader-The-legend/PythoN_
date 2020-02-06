from Peopledata import main as lpd
from SelectionBinary import binary_search as bs
def main():
    people_data = lpd()
    age_key = lambda person: person.age
    age_sorted = sorted(people_data, key=age_key)
    age_result = bs(age_sorted, 69.6, key=age_key)
    print(f"Found index: {age_result}")
    print(f"Person found: {age_sorted[age_result]}")
    def complex_key(person):
        if person.eye_colour == "blue":
            return person.eye_colour + str(person.net_worth)
        else:
            return person.eye_colour
if __name__ == "__main__":
    main()
