# https://codeforces.com/contest/231/submission/308219146

n = int(input())
total_sure = 0
for _ in range(n):
    line = input()
    words = line.split(" ")
    sure_count = 0
    for word in words:
        if word == '1':
            sure_count+=1
    if sure_count >= 2:
        total_sure+=1
print(total_sure)