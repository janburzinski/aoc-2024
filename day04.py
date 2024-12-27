"""
part 1:
- Word search for the word "XMAS"
- word can be horizontal, vertical, diagonal, written backwards or overlapping other words

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

"""

word = "XMAS"
directions = [
    (0, 1),  # horizontal right
    (0, -1),  # horizontal left
    (1, 0),  # vertical down
    (-1, 0),  # vertical up
    (1, 1),  # diagonal down right
    (1, -1),  # diagonal down left
    (-1, 1),  # diagonal up right
    (-1, -1)  # diagonal up left
]


def check_for_xmas(input_data, total_lines, total_cols, i, j, direction):
    dir_x, dir_y = direction
    # loop 4 steps (4 letters in XMAS) in each direction to check if it actually matches the word
    for k, char in enumerate(word):
        # check for the word
        ii = i + k * dir_x
        jj = j + k * dir_y
        # check to not leave the grid
        if not (0 <= ii < total_lines and 0 <= jj < total_cols):
            return False
        if input_data[ii][jj] != char:
            return False
    return True


def check_for_mas_cross(input_data, total_lines, total_cols, i, j):
    # check if the center is within the grid
    if not (1 <= i < total_lines - 1 and 1 <= j < total_cols - 1):
        return False
    # center has to be an A
    if input_data[i][j] != "A":
        return False

    # diagonal down right
    diag_1 = f"{input_data[i - 1][j - 1]}{input_data[i + 1][j + 1]}"
    # diagonal down left
    diag_2 = f"{input_data[i - 1][j + 1]}{input_data[i + 1][j - 1]}"

    # diagonal should be either MS or SM because they are reversable
    if diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]:
        return True

    return False


def part1(input_data):
    solution = 0

    total_lines = len(input_data)
    total_cols = len(input_data[0])

    # iterate through all locations and directions in the grid
    for i in range(total_lines):
        for j in range(total_cols):
            for d in directions:
                solution += check_for_xmas(input_data, total_lines, total_cols, i, j, d)

    return solution


"""
X-MAS:
- find "MAS" in the shape of an X (cross-shape)

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

appearances: 9 times

"""


def part2(input_data):
    solution = 0

    total_lines = len(input_data)
    total_cols = len(input_data[0])

    for i in range(total_lines):
        for j in range(total_cols):
            solution += check_for_mas_cross(input_data, total_lines, total_cols, i, j)

    return solution


"""
X-MAS:
- find "MAS" in the shape of an X (cross-shape)

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

appearances: 9 times

"""

if __name__ == "__main__":
    with open("./inputs/day04.txt") as f:
        data = f.read().strip().split("\n")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
