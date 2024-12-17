"""
part 1:
- ^ represents the guard facing upwards
- # represents obstructions like crates, desks, alchemical reactors etc.

- if "#" in front of me *turn right 90 degrees* "^" => ">" => "v" => "<"

- X represents the visited positions by the guard before leaving the area
"""
from tqdm import tqdm

seen = set()  # stores the x and y coordinates of the positions the guard has been to
dirs = [
    # X  Y
    # hor ver
    [-1, 0],  #
    [0, 1],  #
    [1, 0],  #
    [0, -1]  #
]


def part1(grid):
    global starting_x, starting_y
    current_dir = 0

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

    starting_x = x
    starting_y = y

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
- insert an obstacle so that the guard moves in a loop

- "0" is used to mark the new obstruction
- "|" is used to show a position where the guard moves up/down
- "-" to show a position where the guard moves left/right
- "+" to show a position where the guard moves both up/down and left/right
"""


# test to see if the guard would go into a loop when an obstacle is placed
def test_obstacle(grid, obs_x, obs_y):
    rows = len(grid)
    cols = len(grid[0])

    # check if there is an obstacle at that position already
    if grid[obs_x][obs_y] == "#":
        return False

    # place an obstacle there temporarily
    grid[obs_x][obs_y] = "#"
    x, y = starting_x, starting_y

    # test if the guard would actually go into a loop
    current_dir = 0
    obs_seen = set()  # track the position (x,y) and direction of the guard
    while True:
        # if the guard was at that position already, return to its original state
        # we already know he will loop there
        if (x, y, current_dir) in obs_seen:
            grid[obs_x][obs_y] = "."
            return True

        # add the current position to the seen set
        obs_seen.add((x, y, current_dir))

        # we move up one
        next_x = x + dirs[current_dir][0]  # change in row
        next_y = y + dirs[current_dir][1]  # change in col

        # check for boundaries
        # is that even a viable position to place an obstacle
        if not (0 <= next_x < rows and 0 <= next_y < cols):
            grid[obs_x][obs_y] = "."
            return False

        # make the guard turn right
        if grid[next_x][next_y] == "#":
            current_dir = (current_dir + 1) % 4
        else:
            x, y = next_x, next_y


def part2(input_data):
    solution = 0

    # tqdm is for a little nice animation but can just be ignored
    # e.g. https://gyazo.com/054ec240c7bb76f36e637f7dff5ce3ea
    for obs_x, obs_y in tqdm(seen):

        # if the guard is currently in that position don't test to place an obstacle there
        if obs_x == starting_x and obs_y == starting_y:
            continue

        loop = test_obstacle(input_data, obs_x, obs_y)
        solution += loop

    return solution


if __name__ == "__main__":
    with open("./inputs/day06.txt") as f:
        data = f.read().strip().split("\n")
        grid = [list(line) for line in data]  # so that the strings are mutable

    print("Part 1:", part1(data))
    print("Part 2:", part2(grid))
