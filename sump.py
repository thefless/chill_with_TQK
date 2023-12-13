from array import *

n,q = map(int , input().split())
x = input()
x = '0 ' + x
a = array('i' , map(int , x.split()))
pre = array('i' , [0] * (n + 1))
for i in range(1 , n + 1):
    pre[i] = pre[i - 1] + a[i]

for i in range(q):
    l , r = map(int , input().split())
    print(pre[r] - pre[l - 1])
