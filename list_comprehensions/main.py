"""
https://www.hackerrank.com/challenges/list-comprehensions/problem
"""


def get_list_comp(x_max, y_max, z_max, n):
    return [
        [x, y, z]
        for x in range(x_max + 1)
        for y in range(y_max + 1)
        for z in range(z_max + 1)
        if (x + y + z) != n
    ]


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = get_list_comp(x, y, z, n)
    print(result)
