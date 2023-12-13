from array import *

n = int(input())
a = list(map(int , input().split()))
Sum = 0
count = 0
for i in a:
    if(i > a[n - 1]):
        Sum = Sum + i
        count = count + 1

print(count)
print(Sum)
