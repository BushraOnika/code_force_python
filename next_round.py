n, k = map(int, input().split())
scores = list(map(int, input().split()))
count=0
for i in range(n):
    if(scores[i]>=scores[k-1] and scores[i]>0):
        count+=1
print(count)
