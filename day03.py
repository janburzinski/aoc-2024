"""
- puzzle input seems to be corrupted

- look for input that looks exactly like this mul(2,4)
- something like mul(2,5] is invalid
- max. digits are 3 so max. mul(999,999)
- something like mul( 2, 4 ) would be invalid too

"""
import re

def multiply(report):
    solution = 0
    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    # find all invalid multiply occurrences using the regex
    matches = re.findall(pattern, report)

    for match in matches:
        # extract the two numbers
        inner_content = match[4:-1]
        nums = inner_content.split(",")  # Split into two numbers
        print(f"{nums[0]} - {nums[1]}")  # Print the two numbers

        # multiply the numbers
        if len(nums) < 2:
            print(f"Error with report {match}. not enough numbers provided")
        solution += int(nums[0]) * int(nums[1])

    return solution

def part1(input_data):
    solution = 0

    # split the input data into separate reports to check each report individually
    lines = input_data.splitlines()
    #print("line ", lines)

    for line in lines:
        solution += multiply(line)

    return solution

if __name__ == "__main__":
    with open("./inputs/day03.txt") as f:
         data = f.read().strip()
    print("Part 1:", part1(data))