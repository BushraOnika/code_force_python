n: int = int(input())
x = 0
for _ in range(n):
    line: str = input()
    center = line[len(line) // 2]
    x += 1 if center == '+' else -1
print(x)