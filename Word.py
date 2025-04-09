# Problem link is https://codeforces.com/problemset/problem/59/A
s=input()
count_upper=0
count_lower =0
for char in s:
    if char.isupper() :
        count_upper+=1
    else:
        count_lower+=1

if(count_upper>count_lower):
    print(s.upper())
else:
    print(s.lower())