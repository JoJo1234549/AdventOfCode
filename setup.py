import os

year = input("Type year:\n>>> ")
day = input("Type day:\n>>> ")

folder = f"{year}/{day}"

dir = os.path.dirname(__file__)

path = os.path.join(dir, folder)

print(path)

os.makedirs(path)

os.chdir(path)

try:
    open("__init__.py", "x")
except Exception as e:
    print(e)
    
try:
    open("solution.py", "x")
    f = open("solution.py", "a")
    f.write("""import os

dir = os.path.dirname(__file__)

def read_file(filename):
    file = open(dir + "/" + filename, "r")
    return file.read()""")
except Exception as e:
    print(e)
    
try:    
    open("test_solutions.py", "x")
    f = open("test_solutions.py", "a")
    f.write("""from .solution import read_file

def test_readfile():
    # Arrange

    filename = "sample_input.txt"

    # Act

    result = len(read_file(filename))

    # Assert

    assert result == """)
except Exception as e:
    print(e)
    
try:
    open("input.txt", "x")
except Exception as e:
    print(e)
    
try:
    open("sample_input.txt", "x")
except Exception as e:
    print(e)