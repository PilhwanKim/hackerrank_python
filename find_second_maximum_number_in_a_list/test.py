from utils import read_output_data, read_input_file
from find_second_maximum_number_in_a_list.main import get_second_score


def read_input_data():
    result_list = read_input_file()
    return result_list[0].strip("\n"), list(map(int, result_list[1].split()))


n, arr = read_input_data()
output = read_output_data()

result = get_second_score(arr)

assert result == output
