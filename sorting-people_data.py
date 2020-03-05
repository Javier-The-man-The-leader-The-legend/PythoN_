from Peopledata import main as load_people_data
from pprint import pprint as pp
def main():
    people_data = load_people_data()
    chosen_people = people_data[:40]
    deafault_sort = sorted(chosen_people)
    reversed_default = sorted(chosen_people, reverse=True)
    def networth_fc(person):
        return person.net_worth
    networth_sort = sorted(chosen_people, key=networth_fc)
    # pp(deafault_sort)
    # pp(reversed_default)
    pp(networth_sort)
if __name__ == "__main__":
    main()