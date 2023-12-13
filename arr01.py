from array import *
n = int(input())
a = list(map(int, input().split()))
a = a[::-1]
for i in a:
    print(i , end = " ")