def print_arr(arr):
    for i in range(len(arr)):
        if(len(arr[i])>10):
            print(f"{arr[i][0]}{len(arr[i])-2}{arr[i][-1]}")
        else:
            print(arr[i])

num=int(input())
arr=[]
count=0
while(count<num):
    arr.append(input())
    count+=1
print_arr(arr)
#print(len_arr(arr))

