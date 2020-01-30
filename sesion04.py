moves_count = 0
moves = []
disks_count = int(input())
disks = list(range(1, disks_count + 1))
disks.sort(reverse=True)
sticks = [[], [], []]
sticks[0] = disks
print(sticks)
def move(frm, to):
    last_item = sticks[frm].pop()
    sticks[to].append(last_item)
    moves.append([frm, to])
print(sticks)
def display_game():
    lengths = [len(sticks[0]), len(sticks[1]), len(sticks[2])]
    for i in range(max(lengths), -1, -1):
        first = sticks[0][i] if len(sticks[0]) > i else " "
        second = sticks[1][i] if len(sticks[1]) > i else " "
        third = sticks[2][i] if len(sticks[2]) > i else " "
        print("   {}   {}   {}   ".format(first, second, third))
def solve(number, frm, to, helper):
    if number == 0:
        pass
    else:
        solve(number - 1, frm, helper, to)
        move(frm, to)
        solve(number - 1, helper, to, frm)
display_game()
solve(disks_count, 0, 2, 1)
display_game()
with open("moves.txt", "w") as file:
    file.write(str(moves))