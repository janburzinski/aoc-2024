"""
part 1:
- page number format: X | Y
- first section specifies page ordering rules:
    - e.g. 47|53 => 47 has to be printed before 53, but it does not have to be immediately
- second section specific the page number of each update

rules:
1. every number must be in the same page numbers to update list
"""


# sort the data from the given input into two arrays to
def sort_data(input_data):
    pages_to_update = []
    page_update_rules = []

    # sort the data into the two lists
    for line in input_data:
        if line.strip() == "":  # skip empty lines
            continue
        elif "," in line:  # append lines with "|" => pages to update
            pages_to_update.append(list(map(int, line.strip().split(","))))
        elif "|" in line:  # append lines with "," => page update rules
            page_update_rules.append(list(map(int, line.strip().split("|"))))

    return pages_to_update, page_update_rules


# which page updates are already in the right order
def validate_right_order(page_ordering_rules, page_number_updates):
    # store the correct pairs
    sol = []

    """ check the page ordering rules to make sure that the pages that the pages, that need to be updates, are in the
        correct order in the page numbers to update list
    """
    # loop through all pages that needed to be updates
    # example data: 47|53
    for page_update_rule in page_number_updates:
        valid = True  # we just assume the update is valid initially

        # loop through all the page update rules
        # example data: 75,47,61,53,29
        for page_one, page_two in page_ordering_rules:
            if page_one in page_update_rule and page_two in page_update_rule:
                index_x = page_update_rule.index(page_one)
                index_y = page_update_rule.index(page_two)

                # check if the page_one index is before the page_two index => rule break if true
                if index_x > index_y:  # Rule violated
                    valid = False
                    break

        # all rules were obeyed jaaaaaaaaaa
        if valid:
            sol.append(page_update_rule)

    return sol


def filter_wrong_ordered_updates(page_ordering_rules, page_update_rules):
    sol = []
    correct_update_rules = validate_right_order(page_ordering_rules, page_update_rules)

    # loop over the update rules and filter out the correct ones
    for update_rule in page_ordering_rules:
        # check if the update rule is not in the correct update rules array
        # and add it to the array of wrong updates
        if update_rule not in correct_update_rules:
            sol.append(update_rule)

    return sol


# add up the middle page numbers
# !: only pass the valid ones
def calculate_middle_page_numbers(page_number_updates):
    sol = 0

    """
    check how many numbers are being passed and calculate the median
        => what is the middle
    
    note:
    - arr_len + 1 // 2 - 1 => 1 index based counting is being used for some reason
    
    """
    # calculate the middle number
    # print(page_number_updates)
    for i, arr in enumerate(page_number_updates):
        arr_len = len(arr)
        middle_number = arr_len // 2
        # print(f"i {i} {arr};;; {middle_number} {arr[middle_number]}")
        sol += arr[middle_number]

    return sol


def part1(input_data):
    pages_to_update, page_update_rules = sort_data(input_data)
    solution_one = validate_right_order(page_update_rules, pages_to_update)

    return calculate_middle_page_numbers(solution_one)


if __name__ == "__main__":
    with open("./inputs/day05.txt") as f:
        data = f.read().strip().split("\n")
    print("Part 1:", part1(data))
