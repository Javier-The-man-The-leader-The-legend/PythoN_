instructions = [2,3,4,5,6,7,8]
instructions[1] = 12
instructions[2] = 2
def opcode1(instructions, input1_poistion, input2_poistion, output_poistion):
    input1 = instructions[input1_poistion]
    input2 = instructions[input2_poistion]
    result = input1 + input2

    instructions[output_position] = result
def opcode1(instructions, input1_poistion, input2_poistion, output_poistion):
    input1 = instructions[input1_poistion]
    input2 = instructions[input2_poistion]
    result = input1 * input2

    instructions[output_position] = result
with open("Xmas-2-input.txt", "r") as file:
    contents = file.read().split(",")
instructions = [int(num_as_string) for num_as_string in contents]
for i in range(0, len(instructions), 4):
    opcode = instructions[i]
    if opcode == 1:
        opcode1(i + 1, i + 2, i + 3)
    elif opcode == 2:
        opcode2(i + 1, i + 2, i + 3)
    elif opcode == 99:
        print("instructions")
        exit()