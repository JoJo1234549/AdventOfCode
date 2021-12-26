import os

dir = os.path.dirname(__file__)

def read_file(filename):
    file = open(dir + "/" + filename, "r")
    return file.read()