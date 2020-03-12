def binary_search(data, needle, key=None):
    left_index = 0
    right_index = len(data)
    while right_index - left_index > 1:
        middle_index =  (right_index - left_index) // 2 + left_index
        if key:
            datum = key(data[middle_index])
        else:
            datum = data[middle_index]
        if datum > needle:
            right_index = middle_index
        elif datum < needle:
            left_index = middle_index
        else:
            return middle_index
    print(main(min(numbers)) + 1)
def main(needle):
     with open("data_nums_1000000.txt", "r") as file:
        numbers = list(map(int, file.read().splitlines()))
        numbers.sort()
assert binary_search([4, 8, 15, 16, 23, 43], 15)  == 2, "OMG THE WORLD IS ON FIRE"