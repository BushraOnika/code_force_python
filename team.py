problems=int(input())
total=0
count=0
for _ in range(problems):
    for _ in range(3):
        num=input().split(" ")
        total+=int (num)
    if (total>1):
        count+=1

print(count)

