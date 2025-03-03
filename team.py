problems=int(input())
total=0
count=0
for i in range(problems):
    a =list(map(int,input().split(" ")))
    total+=a[i]
    if(total>1):
        count+=1

print(count)

