# https://codeforces.com/problemset/submission/236/308759043

def solve(name: str):
    """
    >>> solve("wjmzbmr")
    CHAT WITH HER!
    >>> solve("xiaodao")
    IGNORE HIM!
    >>> solve("sevenkplus")
    CHAT WITH HER!
    """
    distinct_characters = set(name)
    print("CHAT WITH HER!") if len(distinct_characters) % 2 == 0 else print("IGNORE HIM!")


if __name__ == '__main__':
    solve(input())