
import array

a = [4,5,6]
b = [7,8,9]
sum=0
for i in range(0,len(a)):
    for i in range(0,len(b)):
        if a[i]>b[i]:
            sum += 1
            print(sum)
        else:
            print(0)
    break 

