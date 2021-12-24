from .solution import plot_lines, read_file, format_data, part1_solution

    # Arrange
    
    # Act
    
    # Assert

def test_readfile():
    # Arrange

    filename = "sample_input.txt"

    # Act

    result = len(read_file(filename).splitlines())

    # Assert

    assert result == 10
    
def test_format_data():
    # Arrange
    
    data = read_file("sample_input.txt")
    
    # Act
    
    result = format_data(data)
    
    # Assert
    
    assert result[0] == [0, 9, 5, 9]
    
def test_plot_lines():
    # Arrange
    
    data = format_data(read_file("sample_input.txt"))
    
    # Act
    
    result = plot_lines(data)
    
    # Assert
    
    assert result["7,4"] == 2

def test_part1_solution():
    # Arrange
    
    data = format_data(read_file("sample_input.txt"))
    points = plot_lines(data)
    
    # Act
    
    result = part1_solution(points)
    
    # Assert
    
    assert result == 5