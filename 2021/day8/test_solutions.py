from .solution import read_file, format_data, part1_solution

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

    assert result[0] == [["be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", "edb"], ["fdgacbe", "cefdb", "cefbgd", "gcbe"]]
    
def test_part1_solution():
    # Arrange
    
    data = format_data(read_file("sample_input.txt"))
    
    # Act
    
    result = part1_solution(data)
    
    # Assert
    
    assert result == 26