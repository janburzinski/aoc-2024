"""
info:
- make free space by compacting all of the files
- format contains: layout of files and free space on the disk.
- digits alternate between indicating the length of a file and the length of free space
- "12345" would represent a one-block file, two blocks of free space, a three block-file, four block of free space, and then a five block file
 => 1: 1 block file
 => 2: 2 blocks of free space
 => 3: 3 block file
 => 4: 4 blocks of free space
 => 5: 5 block file
- 90909 => 3 nine-block files in a row with no free space
    => repeating numbers may match into multiple block files or free space
- each file on the disk also has an id number starting at 0
    => "12345" e.g.
            *type*                *id*
        - 1 block file          0
        - 3 block file          1
        - 5 block file          2

string format:
- one character for each block where
    => digits are the file ID
    => "." is free space
    ---> "12345" => 0..111....22222

task:
- move one file block at a time from the end of the disk to the leftmost free space block
for "12345" it would look like this:
0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222......

solution: filesystem checksum
    => multiply each of the blocks position with the file id number
"""


# string format:
# - one character for each block where
#    => digits are the file ID and represent the blocked space
#    => "." is free space
#    ---> "12345" => 0..111....22222
#    ---> "2333133121414131402" => 00...111...2...333.44.5555.6666.777.888899
def format_string(input_data):
    s = []  # stores the chars of the string
    file_id = 0
    is_file = True

    # go through each number in the string
    for char in input_data:
        b = int(char)  # convert the char into an int. this would be the num of blocks to multiply with
        # is the char supposed to reference to an x-block file
        if is_file:
            s += [file_id] * b  # convert idx to string and write it to the string b times
            file_id += 1  # increase idx
        else:
            # it is supposed to represent free space on the disk
            s += [None] * b  # write "." b amount of times
        is_file = not is_file  # string always starts with is_file so change the bool after each char

    return s  # convert chars back to a normal string


# move file blocks on at a time from the end of the disk to the leftmost free space block until no gaps remain
"""
- reverse the string to get the last element

e.g. string: 
before: 2333133121414131402
after: 0099811188827773336446555566..............
"""


def clear_gaps(disk_map):
    # calc free space we have at the front of the file system
    # this is to keep track of where to insert the next file
    first_free = 0
    while disk_map[first_free] is not None:
        first_free += 1

    # which index do we want to move
    i = len(disk_map) - 1
    while disk_map[i] is None:
        i -= 1

    while i > first_free:
        # swap values
        disk_map[first_free] = disk_map[i]
        disk_map[i] = None
        while disk_map[i] is None:
            i -= 1
        while disk_map[first_free] is not None:
            first_free += 1

    return disk_map


def calc_checksum(disk_map):
    solution = 0

    for i, x in enumerate(disk_map):
        if x is not None:
            solution += i * x
        # print(f"{i} * {int(x)} = {solution}")

    return solution


def part1(input_data):
    disk_map = format_string(input_data)
    print("diskmap:", disk_map)

    moved = clear_gaps(disk_map)
    print("moved", moved)

    return calc_checksum(moved)


def part2(input_data):
    solution = 0
    return solution


if __name__ == "__main__":
    with open("./inputs/day09.txt") as f:
        data = f.read().strip()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
