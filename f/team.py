# https://codeforces.com/problemset/submission/231/309166989

def team(problems_surety: list[int], need_for_being_sure: int = 2) -> bool:
    """
    :return:
    (True | Flase) if team sure

    >>> team([1, 1 ,1])
    True
    >>> team([1, 1 ,0])
    True
    >>> team([1, 0 ,0])
    False
    """

    return sum(problems_surety) >= need_for_being_sure


if __name__ == '__main__':
    n = int(input())
    sure_count = 0
    for i in range(n):
        line = input()
        sure_flag = map(int, line.split(" "))
        if team(sure_flag):
            sure_count += 1
    print(sure_count)
