import json


def read_output_file(filename="output00.txt"):
    with open("./data/output/" + filename, "r") as f:
        return f.readline()


def read_input_file(filename="input00.txt"):
    with open("./data/input/" + filename, "r") as f:
        return f.readlines()


def read_output_data(filename="output00.txt"):
    return json.loads(read_output_file(filename))

