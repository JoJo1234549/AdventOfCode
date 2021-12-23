with open("input.txt") as f:
    _input = f.read().split("\n")

## Part 1 ##

print("Part 1")

larger = 0

for index, i in enumerate(_input):
    try:
        if int(i) > int(_input[index - 1]):
            larger += 1
    except IndexError:
        pass

print(larger)

## Part 2 ##

print("Part 2")

larger = 0

def add_three(index):
    return int(_input[index]) + int(_input[index - 1]) + int(_input[index - 2])

for index, i in enumerate(_input):
    try:
        if add_three(index) > add_three(index - 1):
            larger += 1
    except IndexError:
        pass

print(larger)