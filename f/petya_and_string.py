# https://codeforces.com/problemset/submission/112/309178593

def petya_and_string(a: str, b: str):
    """
    :param a:
    :param b:
    :return:
    lexicographically sign compare of 2 string

    >>> petya_and_string("aaaa", "aaaA")
    0
    >>> petya_and_string("abs", "Abz")
    -1
    >>> petya_and_string("abcdefg", "AbCdEfF")
    1
    """
    a_lower = a.lower()
    b_lower = b.lower()
    if a_lower == b_lower:
        return 0
    else:
        return -1 if a_lower < b_lower else 1

if __name__ == '__main__':
    a = input()
    b = input()
    print(petya_and_string(a, b))