"""
part 1 - Garden Plots need Fencing:
- each plot is indicated by single letter
- if multiple garden plots are growing the same type of plant and are touching => they become a REGION
- area of a region => number of garden plots the region contains
- garden plots are always a square and have four sides

+-+-+-+-+
|A A A A|
+-+-+-+-+     +-+
              |D|
+-+-+   +-+   +-+
|B B|   |C|
+   +   + +-+
|B B|   |C C|
+-+-+   +-+ +
          |C|
+-+-+-+   +-+
|E E E|
+-+-+-+

"""
from collections import deque

with open("./inputs/day12.txt") as f:
    data = f.read().strip().split("\n")

rows = len(data)
cols = len(data[0])
directions = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]


# check if coordinate is within the grid
def in_grid(i, j):
    return (0 <= i < rows) and (0 <= j < rows)


#
# AAAA
# BBCD
# BBCC
# EEEC
#
seen = set()
plots = []

for i in range(rows):
    for j in range(cols):
        # has the plot already been checked? don't consider it
        if (i, j) in seen:
            continue

        stack = [(i, j)]  # initialize stack with starting coordinate
        plots.append([data[i][j], []])  # save the character of the plot and the coordinates (empty array here)

        # DFS
        while stack:
            ci, cj = stack.pop()  # remove the top element and return the given character
            if (ci, cj) in seen:
                continue
            if not in_grid(ci, cj):  # must be within the bounds of the grid
                continue
            if data[ci][cj] != data[i][j]:  # character has to be the same
                continue
            seen.add((ci, cj))

            # update the plot we are currently looking at
            plots[-1][1].append((ci, cj))
            # check all of its neighbours
            for di, dj in directions:
                ii, jj = ci + di, cj + dj
                stack.append((ii, jj))


def count_free(i, j):
    free_sides = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if not in_grid(ni, nj) or data[ni][nj] != data[i][j]:
            free_sides += 1
    return free_sides


def perimeter(plot):
    return sum(count_free(i, j) for i, j in plot)


# part 1
sol = 0

for x, plot in plots:
    print(x, plot, perimeter(plot))
    sol += perimeter(plot) * len(plot)

print(sol)
