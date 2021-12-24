from solution import read_file, format_data, is_win, bingo_sim, part1_solution, part2_solution

    # Arrange
    
    # Act
    
    # Assert

def test_readfile():
    # Arrange

    filename = "sample_input.txt"

    # Act

    result = len(read_file(filename).splitlines())

    # Assert

    assert result == 19

def test_format_data():
    # Arrange

    _input = read_file("sample_input.txt")

    # Act

    result = format_data(_input)

    # Assert
    
    assert result[0] == [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    assert result[1][0] == [[22,13,17,11,0], [8,2,23,4,24], [21,9,14,16,7], [6,10,3,18,5], [1,12,20,15,19]]

def test_is_win():
    # Arrange
    
    board = [[14,21,17,24,4], [10,16,15,9,19], [18,8,23,26,20], [22,11,13,6,5], [2,0,12,3,7]]
    
    # Act
    
    # Assert
    
    assert is_win([7,4,9,5,11,17,23,2,0,14,21,24], board) == True
    assert is_win([7,4,9,5,11,17,23,2,0,14], board) == False
    assert is_win([7,4,9,5,11,18,23,2,0,14,10,22], board) == True
    assert is_win([7,4,9,5,11,18,23,2,0,14], board) == False

def test_bingo_sim():
    # Arrange
    
    _input = read_file("sample_input.txt")
    data = format_data(_input)
    
    # Act
    
    # Assert
    
    assert bingo_sim(data[0], data[1][2]) == [[[14,21,17,24,4], [10,16,15,9,19], [18,8,23,26,20], [22,11,13,6,5], [2,0,12,3,7]], 11]
    assert bingo_sim(data[0], data[1][0]) == [[[22,13,17,11,0], [8,2,23,4,24], [21,9,14,16,7], [6,10,3,18,5], [1,12,20,15,19]], 13]

def test_part1_solution():
    # Arrange

    filename = "sample_input.txt"
    _input = read_file(filename)

    # Act

    result = part1_solution(_input)
    
    # Assert

    assert result == 4512

def test_part2_solution():
    # Arrange

    filename = "sample_input.txt"
    _input = read_file(filename)

    # Act

    result = part2_solution(_input)
    
    # Assert

    assert result == 1924