from array import *

n , k = map(int , input().split())
pre = array('i' , [0] * (2 * n + 1))
x = input()
x = "0 " + x
a = array('i', map(int, x.split()))

for i in range(1 , n):
    a.append(a[i])

for i in range(1 , 2 * n):
    pre[i] = pre[i - 1] + a[i]
Max = -1e18
for i in range(k , 2 * n):
    Max = max(Max , pre[i] - pre[i - k])   
print(Max)