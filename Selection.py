def main(needle):
    with open("data_nums_1000000.txt", "r") as file:
        numbers = map(int, file.read().splitlines())
        for index, n in enumerate(numbers):
            if n == needle:
                return index
print(main(30758376) +1)
                