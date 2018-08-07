"""
https://www.hackerrank.com/challenges/nested-list/problem
"""
from functools import reduce


def convert_list(ret_dict, element):
    if element[1] in ret_dict:
        value_list = ret_dict.get(element[1])
        value_list.append(element[0])
    else:
        ret_dict[element[1]] = [element[0]]
    return ret_dict


def get_second_lowest_grade(grades):
    reduced_dict = reduce(convert_list, grades, {})
    sorted_x = sorted(reduced_dict.items(), key=lambda kv: kv[0])
    return sorted(sorted_x[1][1])


if __name__ == '__main__':
    grade_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade_list.append([name, score])

    result = get_second_lowest_grade(grade_list)

    for ele in result:
        print(ele)
