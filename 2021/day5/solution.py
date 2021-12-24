import os

dir = os.path.dirname(__file__)

def read_file(filename):
    file = open(dir + "/" + filename, "r")
    return file.read()

def format_data(data):
    lines = data.splitlines()
    coords = [[int(value) for value in line.replace(" -> ", ",").split(",")] for line in lines]
    
    return coords

def plot_lines(lines):
    points = {}
    
    def add_point(point):
        try:
            points[f"{point[0]},{point[1]}"] += 1
        except KeyError:
            points[f"{point[0]},{point[1]}"] = 1
    
    for x1, y1, x2, y2 in lines:
        if x1 == x2: # Vertical
            if x1 == x2 and y1 == y2:
                add_point([x1, y1])
            else:
                for i in range(y1 if y1 < y2 else y2, y1 + 1 if y1 > y2 else y2 + 1):
                    add_point([x1, i])
        elif y1 == y2: # Horizontal
            if x1 == x2 and y1 == y2:
                add_point([x1, y1])
            else:
                for i in range(x1 if x1 < x2 else x2, x1 + 1 if x1 > x2 else x2 + 1):
                    add_point([i, y1])
                    
    return points

def part1_solution(points):
    total = 0
    for x in points.values():
        total += 1 if x >= 2 else 0
        
    return total

print(part1_solution(plot_lines(format_data(read_file("input.txt")))))