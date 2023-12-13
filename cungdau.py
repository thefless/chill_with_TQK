from array import *

n = int(input())

x = input()
x = "0 " + x
a = array('i' , map(int , x.split()))

for i in range(2 , n + 1):
    if a[i] * a[i - 1] > 0:
        print(a[i - 1] , a[i])
        exit()
