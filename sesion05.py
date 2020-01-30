import random
# data = []
# for i in range(100):
    # data.append(random.randint(0,100))
# Generator Expression
data = [random.randint(0,100) for _ in range(50)]
# data = [i for i in range(50)]
# print(str(data))
def bubble(data, start_first, start_second):
    num_of_loops = 0
    num_of_swaps = 0
    for j in range(start_first, len(data) - 1):
        # sorted_data = data.sort()
        swaps_before = num_of_swaps
        for i in range(start_second, len(data) - j - 1):
            num_of_loops += 1
            # The next two values out of the list
            first = data[i]
            second = data[i + 1]
            if first > second:
                num_of_swaps += 1
                # data[i] = second                                         
                # data[i + 1] = first
                data[i], data[i + 1] = second, first
                return j, i
        # if sorted_data == data:
            # break
        if swaps_before == num_of_swaps:
            return j, 0
    print("Number of loops {}".format(num_of_loops))
    print("Number of swaps {}".format(num_of_swaps))
if __name__ == "__main__":
    # print(data)
    bubble(data, start_first, start_second)
    # print(data)
    data = [i for i in range(200)]
    bubble(data, start_first, start_second)
    # print(data)
    data = [random.randint(0, 100) if i < 500 else i for i in range(2)]
    bubble(data, start_first, start_second)