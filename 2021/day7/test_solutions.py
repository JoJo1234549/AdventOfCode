from .solution import part1_solution, part2_solution, read_file, format_data, find_mean, find_st_dev, calc_fuel, calc_compound_fuel

def test_readfile():
    # Arrange

    filename = "sample_input.txt"

    # Act

    result = len(read_file(filename).split(","))

    # Assert

    assert result == 10
    
def test_format_data():
    # Arrange
    
    data = read_file("sample_input.txt")
    
    # Act
    
    result = format_data(data)
    
    # Assert
    
    assert result == [16,1,2,0,4,2,7,1,2,14]
    
def test_find_mean():
    # Arrange
    
    data = format_data(read_file("sample_input.txt"))
    
    # Act
    
    result = find_mean(data)
    
    # Assert
    
    assert result == 4.9
    
def test_find_st_dev():
    # Arrange
    
    data = format_data(read_file("sample_input.txt"))
    
    # Act
    
    result = find_st_dev(data)
    
    # Assert
    
    assert result == 5.39351462406472
    
def test_calc_fuel():
    # Arrange
    
    data = format_data(read_file("sample_input.txt"))
    
    # Act
    
    result = calc_fuel(data, 2)
    
    # Assert
    
    assert result == 37
    
def test_calc_compound_fuel():
    # Arrange
    
    data = format_data(read_file("sample_input.txt"))
    
    # Act
    
    result = calc_compound_fuel(data, )
    
    # Assert
    
    assert result == 168
    
def test_part1_solution():
    # Arrange
    
    data = format_data(read_file("sample_input.txt"))
    
    # Act
    
    result = part1_solution(data)
    
    # Assert
    
    assert result == 37
    
def test_part2_solution():
    # Arrange
    
    data = format_data(read_file("sample_input.txt"))
    
    # Act
    
    result = part2_solution(data)
    
    # Assert
    
    assert result == 168