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

    lines = input_data.splitlines()

    # sort the data into the two lists
    for line in lines:
        left_and_right_line = line.split()
        if len(left_and_right_line) == 2:
            left_list.append(int(left_and_right_line[0]))
            right_list.append(int(left_and_right_line[1]))

    # sort the lists so that no negative numbers can be created
    left_list.sort()
    right_list.sort()

    # calculate the distances
    for left, right in zip(left_list, right_list):
        solution += abs(right-left)

    return solution

if __name__ == "__main__":
    with open("./inputs/day01.txt") as f:
        data = f.read().strip()
    print("Part 1:", part1(data))