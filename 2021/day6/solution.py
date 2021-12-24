import os

dir = os.path.dirname(__file__)

def read_file(filename):
    file = open(dir + "/" + filename, "r")
    return file.read()

def format_data(data):
    return [int(value) for value in data.split(",")]

def calc_day(fishies):
    new_fish = []
    for fish in fishies:
        if fish == 0:
            new_fish.append(6)
            new_fish.append(8)
        elif fish > 0:
            new_fish.append(fish - 1)
            
    return new_fish

def calc_days_dict(fishies, days):
    fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for fish in fishies:
        fish_dict[fish] += 1
    
    for i in range(days):
        fish_dict = {8: fish_dict[0],
                     7: fish_dict[8],
                     6: fish_dict[7] + fish_dict[0],
                     5: fish_dict[6],
                     4: fish_dict[5],
                     3: fish_dict[4],
                     2: fish_dict[3],
                     1: fish_dict[2],
                     0: fish_dict[1]
                     }
    return fish_dict

def part1_solution(fishies):
    for i in range(80):
        fishies = calc_day(fishies)
    
    return len(fishies)

def part2_solution(fishies):
    fishies = calc_days_dict(fishies, 256)
    
    return sum(fishies.values())

print(part1_solution(format_data(read_file("input.txt"))))

print(part2_solution(format_data(read_file("input.txt"))))