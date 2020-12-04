
def solve_part_1():
    with open('data/day_1_input.txt', 'r') as f:
        entries = list(map(int, f.read().splitlines()))

        for i in range(len(entries)):
            x = entries[i]
            for y in entries[i:]:
                if (x + y == 2020 and x != y ):
                    return x, y, x*y
        return "no such nums"

def solve_part_2():
    with open('data/day_1_input.txt', 'r') as f:
        entries = list(map(int, f.read().splitlines()))

        for i in range(len(entries)):
            x = entries[i]
            for j in range(len(entries[(i):])):
                y = entries[j]
                for z in entries[j:]:
                    if (x + y + z == 2020):
                        return x, y, z, x*y*z
        return "no such nums"

print(solve_part_2())