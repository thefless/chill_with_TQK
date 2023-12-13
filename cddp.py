from array import *

n = int(input())

x = input()
x = "0 " + x
a = array('i' , map(int , x.split()))

count = 0
for i in range(2 , n):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        count += 1

print(count)