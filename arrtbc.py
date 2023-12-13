n = int(input())
a = list(map(int , input().split()))
tbc = 0
count = 0
check = False

for i in a:
    tbc = tbc + i
tbc = tbc / n 

for i in a:
    if(i > tbc):
        count = count + i
        check = True

if(check == 0):
    print(-1)
else:
    print(count)
