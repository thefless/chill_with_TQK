n = int(input())
a = list(map(int , input().split()))
k = int(input())
check = 0
for i in range(0 , n , 1):
    if a[i] == k:
        print(i + 1 , end = " ")
        check = 1
if check == 0:
    print(-1)
