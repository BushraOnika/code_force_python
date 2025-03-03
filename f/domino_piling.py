# https://codeforces.com/problemset/submission/50/308761285

def domino_piling(m, n)-> int:
    """
    :param m: width maybe
    :param n: height maybe
    :return: (2, 1) domino required

    >>> domino_piling(2, 4)
    4
    >>> domino_piling(3, 3)
    4
    """

    domino_size = (2, 1)
    board_area = m * n
    domino_area = domino_size[0] * domino_size[1]
    min_fit = board_area // domino_area
    return min_fit


if __name__ == '__main__':
    m, n = map(int, input().split(" "))
    print(domino_piling(m, n))
