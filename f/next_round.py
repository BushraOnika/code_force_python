# https://codeforces.com/problemset/submission/158/309174985

def next_round(k: int, a: list[int]) -> int:
    """
    :param k: ordinal of selected participant
    :param a: score of particepets
    :return:
    number of participants who advance to the next round

    >>> next_round(5, [int(word) for word in "10 9 8 7 7 7 5 5".split(" ")])
    6
    >>> next_round(2, [int(word) for word in "0 0 0 0".split(" ")])
    0

    """
    kth_participants_score = a[k - 1]
    qualified_count = 0
    for score in a:
        if 0 < score >= kth_participants_score:
            qualified_count += 1

    return qualified_count


if __name__ == '__main__':
    line_1 = input()
    n, k = [int(word) for word in line_1.split(" ")]

    line_2 = input()
    a = [int(word) for word in line_2.split(" ")]

    qualified_count = next_round(k, a)
    print(qualified_count)
