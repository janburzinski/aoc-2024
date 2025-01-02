"""
- two buttons: A | B
cost per push:
- button a: 3 tokens
- button b: 1 token

- each push moves the claw a specific amount to the right (x axis) and a specific amount forward (y axis)
- each machine contains ONE prize
    => to win: claw must be positioned exactly above the prize on x and y axis

task:
Figure out how to win as many prizes as possible.
What is the fewest tokens you would have to spend to win all possible prizes?
"""

"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

moves:
- push button A moves the claw 94 units along the X Axis and 34 along the Y Axis
- push button B moves the claw 22 units along the X Axios and 67 along the Y Axis
- prize is located at X=8400 Y=5400

solution:
- push button A: 80 times and  button B: 40 times (x: 80*94 + 40*22 = 8400) (y: 80*34 + 40*67 = 5400)

"""

with open("./day13.txt") as f:
    data = f.read().strip().split("\n\n")


# ! this method should/could also be done using regex !
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
def parse(input):
    # stores x and y coordinate
    # so the length of each array will be 1 (2)
    button_a = []  # movements for (X-Axis, Y-Axis)
    button_b = []  # ''
    prize = []  # (X,Y)
    for line in input.splitlines():
        if line.startswith("Button A:"):
            cords = line.replace("Button A:", "").replace("X+", "").replace("Y+", "").strip().split(", ")
            button_a.append(int(cords[0]))
            button_a.append(int(cords[1]))
        elif line.startswith("Button B:"):
            cords = line.replace("Button B:", "").replace("X+", "").replace("Y+", "").strip().split(", ")
            button_b.append(int(cords[0]))
            button_b.append(int(cords[1]))
        elif line.startswith("Prize:"):
            cords = line.replace("Prize: ", "").replace("X=", "").replace("Y=", "").strip().split(", ")
            prize.append(int(cords[0]))
            prize.append(int(cords[1]))
    # print(f"{button_a} {button_b} {prize}")
    print(button_a)

    return button_a, button_b, prize


prices = []
for b_a, b_b, pri in [parse(input=line) for line in data]:
    # test to see if reaching the prize is actually doable with the amount of pushes
    # i and j will be a num from 0-100
    def test_tuple(i, j):
        x = b_a[0] * i + b_b[0] * j
        y = b_a[1] * i + b_b[1] * j
        return (x, y) == tuple(pri)


    v = 1 << 30  # shifts the binary of 1 to the left by 30 positions (basically adds 30 x '0')
    for i in range(100):
        for j in range(100):
            if test_tuple(i, j):
                v = min(v, 3 * i + j)

    if v < 1 << 30:
        prices.append(v)

spent = 0
print(sum(prices))
