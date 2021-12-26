from .solution import read_file

def test_readfile():
    # Arrange

    filename = "sample_input.txt"

    # Act

    result = len(read_file(filename))

    # Assert

    assert result == 