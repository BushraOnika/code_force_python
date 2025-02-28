count = 0
input_num=int(input())
for _ in range(input_num):
    bit=input()
    if "++" in bit:
        count += 1
    elif "--" in bit:
        count-=1

print(count)