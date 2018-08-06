from utils import read_output_data, read_input_file
from list_comprehensions.main import get_list_comp


def read_input_data(filename="input00.txt"):
    result_list = read_input_file(filename)
    for line in result_list:
        yield int(line.strip("\n"))


x_max, y_max, z_max, n = list(read_input_data())
result = get_list_comp(x_max, y_max, z_max, n)

output = read_output_data()
assert result == output
