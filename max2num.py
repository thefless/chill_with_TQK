from array import *

n = int(input())

x = input()
x = '0 ' + x
a = array('i' , map(int , x.split()))

Min1 = Min2 = 1e18
Max1 = Max2 = -1e18
for i in range(1 , n + 1):
    if a[i] >= Max1:
        Max2 = Max1
        Max1 = a[i]
    elif a[i] >= Max2:
        Max2 = a[i]
    if a[i] <= Min1:
        Min2 = Min1
        Min1 = a[i]
    elif a[i] <= Min2:
        Min2 = a[i]

print(max(Min1 * Min2 , Max1 * Max2))