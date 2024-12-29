"""
part 1:
- each blink the stones simultaneously change
    => 0 is replaced by a stone with the number 1
    => even number is replaced by two stones. left half of the numbers are on the one stone, rest are on the others
        => 1000 -> 10 | 0
        => don't keep leading zeros
    => no rules apply: old stones number is multiplied by 2024
"""


def calc_num(input_data):
    sol = []
    stones = input_data.split(" ")
    print(f"before: {stones}")

    for i, x in enumerate(stones):
        stone = int(x)
        # rule nr. 1
        if stone == 0:
            sol.append(1)
        # rule nr. 2
        # split the two stones in half if the
        elif len(str(stone)) % 2 == 0:
            ss = str(stone)
            mid = len(ss) // 2
            left = int(ss[:mid])
            right = int(ss[mid:])
            sol.append(left)
            sol.append(right)
        # rule nr. 3
        else:
            sol.append(stone * 2024)

    print(f"after: {stones}")

    return sol


def part1(input_data):
    sol = calc_num(input_data)

    for _ in range(24):
        sol = calc_num(" ".join(map(str, sol)))

    return len(sol)


"""
part 2:
-
"""


def part2(input_data):
    solution = 0
    return solution


if __name__ == "__main__":
    with open("./inputs/day11.txt") as f:
        data = f.read().strip()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
