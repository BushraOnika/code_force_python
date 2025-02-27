# https://codeforces.com/problemset/submission/71/308085370

over_flow_after = 10
n = int(input())
for _ in range(n):
    line = input()
    line_len = len(line)
    print(line) if line_len <= over_flow_after else print(line[0], line_len-2, line[-1], sep="")