import os, math

dir = os.path.dirname(__file__)

def read_file(filename):
    file = open(dir + "/" + filename, "r")
    return file.read()

def format_data(data):
    return [int(value) for value in data.split(",")]

def find_mean(positions):
    return sum(positions)/len(positions)

def find_st_dev(values):
    mean = find_mean(values)
    return ((sum([(value - mean)**2 for value in values]) / len(values))**0.5)

def calc_fuel(positions, target):
    total = 0
    for position in positions:
        total += abs(target - position)
    return total

def calc_compound_fuel(positions, target):
    total = 0
    for position in positions:
        total += sum(range(0, abs(target - position) + 1))
    return total

def part1_solution(positions):
    mean = find_mean(positions)
    stdev = find_st_dev(positions)
    minimum = None
    for i in range(max(math.floor(mean-stdev), 0), math.ceil(mean+stdev) + 1):
        fuel = calc_fuel(positions, i)
        if not minimum:
            minimum = fuel
        elif fuel < minimum:
            minimum = fuel
    
    return minimum

def part2_solution(positions):
    mean = find_mean(positions)
    stdev = find_st_dev(positions)
    minimum = None
    for i in range(max(math.floor(mean-stdev), 0), math.ceil(mean+stdev) + 1):
        fuel = calc_compound_fuel(positions, i)
        if not minimum:
            minimum = fuel
        elif fuel < minimum:
            minimum = fuel
    
    return minimum

print(part1_solution(format_data(read_file("input.txt"))))

print(part2_solution(format_data(read_file("input.txt"))))