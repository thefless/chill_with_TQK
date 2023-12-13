from array import *

n , k = map(int , input().split())
x = input()
x = '0 ' + x
a = array('i' , map(int , x.split()))
count = 0

for i in range(1 , n - 1):
    Sum = a[i] + a[i + 1] + a[i + 2]
    Product = a[i] * a[i + 1] * a[i + 2]
    if Product / Sum == k:
        count = count + 1

print(count)