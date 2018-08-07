from utils import read_output_file2, read_input_file
from nested_list.main import get_second_lowest_grade


def read_input_data(filename="input01.txt"):
    result_list = read_input_file(filename)
    rows = int(result_list[0].strip('\n'))
    result = []
    for index in range(rows):
        result.append([result_list[2*index + 1].strip('\n'), float(result_list[2*index + 2].strip('\n'))])
    return result


def read_output_data():
    output_list = read_output_file2("output01.txt")
    output_result_list = []
    for output_ele in output_list:
        output_result_list.append(output_ele.strip('\n'))
    return output_result_list


grade_list = list(read_input_data())
result = get_second_lowest_grade(grade_list)
output = read_output_data()
assert result == output
