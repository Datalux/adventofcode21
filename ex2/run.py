inputs = []

with open("input.txt") as file:
    for line in file:
        inputs.append((line.rstrip().split(" ")))

def test1():
    x = 0
    y = 0
    for pos in inputs:
        if pos[0] == "forward":
            x += int(pos[1])
        elif pos[0] == "down":
            y += int(pos[1])
        else:
            y -= int(pos[1])

    return x*y


def test2():
    x = 0
    y = 0
    aim = 0
    for pos in inputs:
        if pos[0] == "forward":
            x += int(pos[1])
            y += (aim * int(pos[1]))
        elif pos[0] == "down":
            aim += int(pos[1])
        else:
            aim -= int(pos[1])
    
    return x*y


print(test1())
print(test2())