from array import *
n = int(input())
x = list(map(str , input().split()))

for i in x:
    if "10" in i:
        print(i , end = ' ')