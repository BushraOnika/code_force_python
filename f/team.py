# https://codeforces.com/contest/231/submission/308219146

def team(need_for_being_sure: int, problems_surety: list[int]) -> bool:
    """
    :return:
    total sure

    >>>  team(2, [1, 1 ,1])
    True
    >>>  team(2, [1, 1 ,0])
    True
    >>>  team(2, [1, 0 ,0])
    False
    """

    return sum(problems_surety) >= need_for_being_sure


if __name__ == '__main__':
    n = int(input())
    sure_count = 0
    for i in range(n):
        line = input()
        sure_flag = map(int, line.split(" "))
        if team(2, sure_flag):
            sure_count += 1
    print(sure_count)
