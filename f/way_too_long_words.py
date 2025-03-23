# https://codeforces.com/problemset/submission/71/309167025

def way_too_long_words(line: str, over_flow_after=10) -> str:
    """
    :param line:
    :param over_flow_after:
    :return: modified word

    >>> way_too_long_words("word")
    'word'
    >>> way_too_long_words("localization")
    'l10n'
    >>> way_too_long_words("internationalization")
    'i18n'
    >>> way_too_long_words("pneumonoultramicroscopicsilicovolcanoconiosis")
    'p43s'

    """
    line_len = len(line)
    return line if line_len <= over_flow_after else f"{line[0]}{line_len - 2}{line[-1]}"


if __name__ == '__main__':
    over_flow_after = 10
    n = int(input())
    for _ in range(n):
        line = input()
        output = way_too_long_words(line, over_flow_after)
        print(output)
