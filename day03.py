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
    # find all invalid multiply occurrences using the regex
    matches = re.findall(r"mul\(\d+,\d+\)", report)

    for match in matches:
        # extract the two numbers
        inner_content = match[4:-1]

        # Split into the two numbers to multiply
        nums = inner_content.split(",")

        # multiply the numbers
        solution += int(nums[0]) * int(nums[1])

    return solution


"""
part 2:
- adds the do and don't instruction for the multiplication
"""


def multiply_pt2(report):
    solution = 0
    should_multi = False
    is_first_done = False

    # find all invalid multiply occurrences using the regex
    # this time we include the do and don't instruction
    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", report)

    for match in matches:
        # print(match)
        if match == "do()":
            should_multi = True
        elif match == "don't()":
            should_multi = False
        else:  # It's a mul(a,b)
            # check if the first mul is already processed or if you actually got a do() instruction
            if not is_first_done or should_multi:
                is_first_done = True
                # extract the two numbers
                inner_content = match[4:-1]

                # split into the two numbers to multiply
                nums = inner_content.split(",")
                x, y = int(nums[0]), int(nums[1])

                # Add the product to the solution
                solution += x * y

    return solution


def part1(input_data):
    return multiply(input_data)


def part2(input_data):
    return multiply_pt2(input_data)


if __name__ == "__main__":
    with open("./inputs/day03.txt") as f:
        data = f.read().strip()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
