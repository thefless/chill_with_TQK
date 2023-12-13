from array import *

n = int(input())

x = input()
x = '0 ' + x 
a = array('i' , map(int , x.split()))

Max1 = Max2 = -1e18
for i in range(1 , n + 1):
    if a[i] >= Max1:
        Max2 = Max1
        Max1 = a[i]
    elif a[i] >= Max2:
        Max2 = a[i]

print(Max1 + Max2)
