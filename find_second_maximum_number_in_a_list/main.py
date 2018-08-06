"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""


def get_second_score(data_list):
    data_list = list(set(data_list))
    data_list.sort(reverse=True)
    return data_list[1]


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = get_second_score(arr)
    print(result)
