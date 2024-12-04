"""
- data: data consists of many reports, one report per line
- each report is a list of numbers, separated by spaces. e.g.
#1 Report. 7 6 4 2 1
#2 Report. 1 2 7 8 9
#3 Report. 9 7 6 2 1
#4 Report. 1 3 2 4 5
#5 Report. 8 6 4 4 1
#6 Report. 1 3 6 7 9

# A Report only counts of the numbers are ALL increasing or ALL decreasing
# a level can you be different by min. 1 and max. 3
"""

def is_safe(report):
    only_increasing = None

    # split a report by spaces to check each number
    nums = list(map(int, report.split()))

    # check each number
    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]

        # check if the difference between the current number and the number to the right of it is
        # a min. 1 and a max. 3
        # e.g.
        # 1 3 5 => safe
        # 1 6 9 => unsafe
        if not check_adjacent_level_differ(nums[i], nums[i + 1]):
            print(f"{nums[i]} has a too big difference between two numbers")
            return False

        # set the trend for the current report
        if only_increasing is None:
            if diff > 0:
                only_increasing = True
                print(f"{nums[i]} is only increasing")
            elif diff < 0:
                only_increasing = False
                print(f"{nums[i]} is only decreasing")

        # validate the trend
        if only_increasing and diff < 0:
            return False
        if not only_increasing and diff > 0:
            return False

    return True

# the two numbers should only differ by a min. 1 and a max. 3
def check_adjacent_level_differ(num, num2):
    diff = abs(num - num2)
    return 1 <= diff <= 3

def part1(input_data):
    solution = 0

    # split the input data into separate reports to check each report individually
    lines = input_data.splitlines()
    print("line ", lines)

    for line in lines:
        print(f"check {line}")
        if is_safe(line):
            print("safe ", line)
            solution += 1

    return solution

if __name__ == "__main__":
    with open("./inputs/day02.txt") as f:
         data = f.read().strip()
    print("Part 1:", part1(data))