from array import *

n = int(input())

x = input()

x = '0 ' + x

a = array('i' , map(int , x.split()))

tong = 0
for i in range(1 , n + 1):
    tong += a[i]
    print(tong , end = ' ')