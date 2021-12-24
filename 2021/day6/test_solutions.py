from .solution import read_file, format_data, calc_day, calc_days_dict, part1_solution, part2_solution

def test_readfile():
    # Arrange

    filename = "sample_input.txt"

    # Act

    result = len(read_file(filename).split(","))

    # Assert

    assert result == 5
    
def test_format_data():
    # Arrange
    
    data = read_file("sample_input.txt")
    
    # Act
    
    result = format_data(data)
    
    # Assert
    
    assert result == [3,4,3,1,2]
    
def test_calc_day():
    # Arrange
    
    data = read_file("sample_input.txt")
    
    # Act
    
    result = calc_day(format_data(data))
    
    # Assert
    
    assert result == [2, 3, 2, 0, 1]

def test_calc_days_dict():
    # Arrange
    
    data = read_file("sample_input.txt")
    
    # Act
    
    result = calc_days_dict(format_data(data), 1)
    
    # Assert
    
    assert result == {0: 1, 1: 1, 2: 2, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

def test_part1_solution():
    # Arrange
    
    data = read_file("sample_input.txt")
    fish = format_data(data)
    
    # Act
    
    result = part1_solution(fish)
    
    # Assert
    
    assert result == 5934
    
def test_part2_solution():
    # Arrange
    
    data = read_file("sample_input.txt")
    fish = format_data(data)
    
    # Act
    
    result = part2_solution(fish)
    
    # Assert
    
    assert result == 26984457539