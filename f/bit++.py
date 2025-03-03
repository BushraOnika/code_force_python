# https://codeforces.com/problemset/submission/282/308763114

def bit_plus_plus(line: str) -> int:
    """
    :param line:
    Operation ++
    Operation --
    :return:
    "++"  ↦  1 | "--"  ↦  -1

    >>> bit_plus_plus("X++")
    1
    >>> bit_plus_plus("--X")
    -1
    """
    middle_number = len(line) // 2
    middle_char = line[middle_number]
    return 1 if middle_char == '+' else -1


if __name__ == '__main__':
    n: int = int(input())
    x: int = 0
    for _ in range(n):
        line = input()
        x += bit_plus_plus(line)
    print(x)
