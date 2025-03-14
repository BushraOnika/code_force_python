# problem : https://codeforces.com/problemset/problem/546/A
price,amount,bananas=map(int,input().split())
i=1
total=0
while(i<=bananas):
    total+=(i*price)
    i+=1
print(max(0,total-amount))
