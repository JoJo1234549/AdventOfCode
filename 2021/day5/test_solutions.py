from .solution import plot_lines, read_file, format_data, plot_diagonals, draw_diagram, part1_solution, part2_solution

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
    
def test_plot_diagonals():
    # Arrange
    
    data = format_data(read_file("sample_input.txt"))
    points = plot_lines(data)
    
    # Act
    
    result = plot_diagonals(data, points)
    
    # Assert
    
    assert result["4,4"] == 3
    
def test_diagram():
    # Arrange
    
    data = format_data(read_file("sample_input.txt"))
    points = plot_diagonals(data, plot_lines(data))
    
    # Act
    
    result = draw_diagram(points)
    
    # Assert
    
    assert result == """1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111...."""

def test_part1_solution():
    # Arrange
    
    data = format_data(read_file("sample_input.txt"))
    points = plot_lines(data)
    
    # Act
    
    result = part1_solution(points)
    
    # Assert
    
    assert result == 5

def test_part2_solution():
    # Arrange
    
    data = format_data(read_file("sample_input.txt"))
    points = plot_lines(data)
    points = plot_diagonals(data, points)
    
    # Act
    
    result = part2_solution(points)
    
    # Assert
    
    assert result == 12