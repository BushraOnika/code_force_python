# https://codeforces.com/problemset/submission/236/308761267

def boy_or_girl(name: str) -> str:
    """
    :param name: girl or boy name
    :return:
    ("CHAT WITH HER!" | "IGNORE HIM!")

    >>> boy_or_girl("wjmzbmr")
    'CHAT WITH HER!'
    >>> boy_or_girl("xiaodao")
    'IGNORE HIM!'
    >>> boy_or_girl("sevenkplus")
    'CHAT WITH HER!'
    """

    distinct_characters = set(name)
    return "CHAT WITH HER!" if len(distinct_characters) % 2 == 0 else "IGNORE HIM!"


if __name__ == '__main__':
    line = input()
    print(boy_or_girl(line))
