with open("input.txt") as f:
    _input = f.read().split("\n")

## Part 1 ##

print("Part 1")

horizontal = 0
depth = 0

for direction in _input:
    if direction.startswith("forward"):
        horizontal += int(direction.split()[1])
    if direction.startswith("down"):
        depth += int(direction.split()[1])
    if direction.startswith("up"):
        depth -= int(direction.split()[1])

print(f"Horizontal {horizontal}\nDepth {depth}\nCourse {horizontal * depth}")

## Part 2 ##

print("Part 2")

horizontal = 0
depth = 0
aim = 0

for direction in _input:
    if direction.startswith("forward"):
        horizontal += int(direction.split()[1])
        depth += int(direction.split()[1]) * aim
    if direction.startswith("down"):
        # depth += int(direction.split()[1])
        aim += int(direction.split()[1])
    if direction.startswith("up"):
        # depth -= int(direction.split()[1])
        aim -= int(direction.split()[1])

print(f"Horizontal {horizontal}\nDepth {depth}\nAim {aim}\nCourse {horizontal * depth}")