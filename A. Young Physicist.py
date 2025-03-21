#https://codeforces.com/problemset/problem/69/A
num=int (input())
total=0
for _ in range(num):
    arr=map(int,input().split())
    total+= sum(arr)

if(sum==0):
    print("YES")
else:
    print("NO")
