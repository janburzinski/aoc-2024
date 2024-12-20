"""
part 1:
- each line is an equation; test values appear before ":"
- ignore math precedence rules
- operators cannot be rearranged
- only operators to be used are "+" and "*"

- determine if the values can be combined to produce the test value

- solution: total calibration result => sum of test values of the possible equations

problem-solving approach:
- brute force the solution with recursion:
    - just try every possible combination
"""
from tqdm import tqdm
from itertools import product


# we use recursion to solve this problem
def check(equations, calibration_result, current_value=0, idx=0):
    # if true: we checked all equations and now need to check if the solution we got is correct
    if idx == len(equations):
        return current_value == calibration_result

    # add the current number at equations[idx] to the current value
    equation = current_value + equations[idx]
    if check(equations, calibration_result, equation, idx + 1):
        return True

    # multiply the current number at equations[idx] with the current value
    # if the current value is 0 use the number at equations[idx] to avoid making the whole solution be 0
    equation = current_value * equations[idx] if current_value != 0 else equations[idx]
    if check(equations, calibration_result, equation,
             idx + 1):
        return True

    # Nothing worked :(
    return False


# the difference here is that there is now the possibility of a merge of the two numbers
# the number and the number to the right of it can now be merged into one
# e.g. 12 || 345 => 12345
def check_p2(equations, calibration_result, current_value=0, idx=0):
    # if true: we checked all equations and now need to check if the solution we got is correct
    if idx == len(equations):
        return current_value == calibration_result
    print(
        f"DEBUG: idx={idx}, current_value={current_value}, remaining_equations={equations[idx:]}, target={calibration_result}")

    # add the current number at equations[idx] to the current value
    # e.g. 1 + 12 = 13
    if check_p2(equations, calibration_result, current_value + equations[idx], idx + 1):
        return True

    # multiply the current number at equations[idx] with the current value
    # if the current value is 0 use the number at equations[idx] to avoid making the whole solution be 0
    # e.g. 1 * 2 = 2
    if check_p2(equations, calibration_result, current_value * equations[idx] if current_value != 0 else equations[idx],
                idx + 1):
        return True

    """
    combination of two numbers
    """
    # new possibility "||" => concatenate current and next number, if possible
    if idx + 1 < len(equations):
        merged_value = int(f"{equations[idx]}{equations[idx + 1]}")  # merge the number and number next to it
        # print(f"trying concat: 1: {equations[idx]} 2: {equations[idx + 1]} m: {merged_value}")
        if check_p2(equations, calibration_result, merged_value, idx + 2):
            return True

        # addition
        if check_p2(equations, calibration_result, current_value + merged_value, idx + 2):
            return True

        # multiplication
        if check_p2(equations, calibration_result, current_value * merged_value if current_value != 0 else merged_value,
                    idx + 2):
            return True

    # Nothing worked :(
    return False


def part1(input_data):
    solution = 0

    # split the string "3267: 81 40 27" into the calibration result and the equation
    for line in input_data:
        # split the input string into the two different parts
        parts = line.split(":", 1)
        calibration_result = int(parts[0].strip())
        equations = []
        for num in parts[1].strip().split():
            equations.append(int(num))

        # check if the given equation can result to the calibration result
        # if true: add the calibration result to the solution
        if check(equations, calibration_result):
            solution += calibration_result

    return solution


"""
part 2:
"""


def part2(input_data):
    ans = 0
    for i, line in enumerate(input_data):
        parts = line.split()
        value = int(parts[0][:-1])
        nums = list(map(int, parts[1:]))

        def test(combo):
            ans = nums[0]
            for i in range(1, len(nums)):
                if combo[i - 1] == "+":
                    ans += nums[i]
                elif combo[i - 1] == "|":
                    ans = int(f"{ans}{nums[i]}")
                else:
                    ans *= nums[i]
            return ans

        for combo in product("*+|", repeat=len(nums) - 1):
            if test(combo) == value:
                print(f"[{i:02}/{len(input_data)}] WORKS", combo, value)
                ans += value
                break

    return ans


if __name__ == "__main__":
    with open("./inputs/day07.txt") as f:
        data = f.read().strip().split("\n")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
