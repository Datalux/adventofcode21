inputs = []

with open("input.txt") as file:
    for line in file:
        inputs.append(int(line.rstrip()))


def test1():
    counter = 0
    for idx in range(1, len(inputs)):
        if inputs[idx] > inputs[idx-1]:
            counter += 1

    return counter


def test2():
    counter = 0
    for idx in range(len(inputs)):
        s1 = sum(inputs[idx:idx+3])
        s2 = sum(inputs[idx+1:idx+4])
        if(s2 > s1):
            counter += 1
    
    return counter

print(test1())
print(test2())