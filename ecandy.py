from array import *
n = int(input())
x = input()
a = array('i' , map(int , x.split()))

Min = min(a)
Sum = 0
for i in a:
    Sum += i - Min

print(Sum)