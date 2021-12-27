import os

dir = os.path.dirname(__file__)

def read_file(filename):
    file = open(dir + "/" + filename, "r")
    return file.read()

def format_data(data):
    lines = data.splitlines()
    split = [[section.split() for section in line.split("|")] for line in lines]
    return split

def part1_solution(data):
    total = 0
    for entry, output in data:
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                total += 1
                
    return total

print(part1_solution(format_data(read_file("input.txt"))))