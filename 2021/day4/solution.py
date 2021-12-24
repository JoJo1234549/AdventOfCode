import os

dir = os.path.dirname(__file__)

def read_file(filename):
    file = open(dir + "/" + filename, "r")
    return file.read()

def format_data(data):
    parts = data.split("\n\n")
    bingo_numbers = [int(value) for value in parts[0].split(",")]

    bingo_grids = parts[1:]

    bingo_grids = [grid.split("\n") for grid in bingo_grids]
    bingo_grids = [[[int(value) for value in line.split()] for line in grid] for grid in bingo_grids]
    
    return [bingo_numbers, bingo_grids]

def is_win(numbers, board):
    for row in board:
        complete = True
        for num in row:
            if num not in numbers:
                complete = False
                break
        if complete == True:
            return True
    
    for column in range(5):
        complete = True
        for row in board:
            if row[column] not in numbers:
                complete = False
                break
        if complete == True:
            return True
    
    return False

def bingo_sim(numbers, board):
    for index, number in enumerate(numbers):
        status = is_win(numbers[:index + 1], board)
        if status == True:
            return [board, index]
    return [board, None]

def part1_solution(_input):
    numbers, boards = format_data(_input)
    quickest = [None, None]
    for board in boards:
        sim_board, win_index = bingo_sim(numbers, board)
        if not quickest[1]:
            quickest = [board, win_index]
        if win_index and win_index < quickest[1]:
            quickest = [board, win_index]
    
    board_numbers = sum(quickest[0], [])
    for number in numbers[:quickest[1] + 1]:
        try:
            board_numbers.remove(number)
        except ValueError:
            pass
    
    score = sum(board_numbers) * numbers[quickest[1]]
    return score

def part2_solution(_input):
    numbers, boards = format_data(_input)
    slowest = [None, None]
    for board in boards:
        sim_board, win_index = bingo_sim(numbers, board)
        if not slowest[1]:
            slowest = [board, win_index]
        if win_index and win_index > slowest[1]:
            slowest = [board, win_index]
    
    board_numbers = sum(slowest[0], [])
    for number in numbers[:slowest[1] + 1]:
        try:
            board_numbers.remove(number)
        except ValueError:
            pass
    
    score = sum(board_numbers) * numbers[slowest[1]]
    return score

print(part1_solution(read_file("input.txt")))

print(part2_solution(read_file("input.txt")))