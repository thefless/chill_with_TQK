from array import *

n = int(input())
x1 = '0 ' + input()
x2 = '0 ' + input()

a = array('i' , map(int , x1.split()))
b = array('i' , map(int , x2.split()))
prea = array('i' , [0] * (n + 2))
preb = array('i' , [0] * (n + 2))

for i in range(1 , n + 1):
    prea[i] = prea[i - 1] + a[i]
for i in range(n , 0 , -1):
    preb[i] = preb[i + 1] + b[i]
Max = -1e18
for i in range(0 , n + 1):
    Max = max(Max , prea[i] + preb[i + 1])
    # print(i , prea[i] , preb[i + 1] , prea[i] + preb[i + 1])

print(Max)