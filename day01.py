# - visit locations and mark it as visited when checked
# -> just a list with the locations and a list with the checked locations
# - first location is the chief historian's office
# => office is empty, and he is nowhere to be found
# - list is found with location ids

## TASK ##
# figure out the distance between two numbers from two lists
# left list is only the smaller numbers with the smallest number being 1
# right list is only bigger numbers with the smallest being 3
# add up all the distances

def part1(input_data):
    solution = 0
    left_list = []
    right_list = []

    # sort the data into the two lists
    for line in input_data:
        left_and_right_line = line.split()
        if len(left_and_right_line) == 2:
            left_list.append(int(left_and_right_line[0]))
            right_list.append(int(left_and_right_line[1]))

    # sort the lists so that no negative numbers can be created
    left_list.sort()
    right_list.sort()

    # calculate the distances
    for left, right in zip(left_list, right_list):
        solution += abs(right - left)

    return solution


"""
### calculating similarity score ###
- check how often nums from the left list appear in the right list
- 

calc:
- x * num of appearances in the right list = similarity score 
"""


def scan_list_for_num(right_list_input, num):
    appearances = 0  # keep track of how often the num appeared

    # scan for num
    for n in right_list_input:
        if num == n:
            appearances += 1
            print("found", n, appearances)

    print(f"{n} appeared {appearances}")

    # calc score
    return num * appearances


def part2(input_data):
    sol = 0
    left_list = []
    right_list = []

    for line in input_data:
        # split data into lists
        lr = line.split()
        if len(lr) < 2:
            break
        left_list.append(int(lr[0]))
        right_list.append(int(lr[1]))

    for n in left_list:
        sol += scan_list_for_num(right_list, n)

    return sol


if __name__ == "__main__":
    with open("./inputs/day01.txt") as f:
        data = f.read().strip().split("\n")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
