"""
part 1:
- ^ represents the guard facing upwards
- # represents obstructions like crates, desks, alchemical reactors etc.

- if "#" in front of me *turn right 90 degrees* "^" => ">" => "v" => "<"

- X represents the visited positions by the guard before leaving the area

problem-solving approach:
-
"""


def part1(grid):
    seen = set()  # stores the x and y coordinates of the positions the guard has been to
    current_dir = 0
    dirs = [
        # X  Y
        # hor ver
        [-1, 0],  #
        [0, 1],  #
        [1, 0],  #
        [0, -1]  #
    ]

    rows = len(grid)
    cols = len(grid[0])

    # determine starting location
    found = False
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "^":
                found = True
                break

        if found:
            break

    while True:
        # store the x and y coordinate
        # would represent the "X" in the grid basically
        seen.add((x, y))

        # we move up one
        next_x = x + dirs[current_dir][0]  # change in row
        next_y = y + dirs[current_dir][1]  # change in col

        # check for boundaries
        # this basically checks if we hit the edge of the grid, in which case we could be finished and can break
        if not (0 <= next_x < rows and 0 <= next_y < rows):
            break

        # we hit an obstruction
        if grid[next_x][next_y] == "#":
            current_dir = (current_dir + 1) % 4
        else:
            x, y = next_x, next_y

    return len(seen)


"""
part 2:
- 

problem-solving approach:
"""


def part2(input_data):
    solution = 0
    return solution


if __name__ == "__main__":
    with open("./inputs/day06.txt") as f:
        data = f.read().strip().split("\n")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
