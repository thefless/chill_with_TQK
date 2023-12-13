n = int(input())

a = list(map(int , input().split()))

Min = min(a)
Max = max(a)
print(Min , a.count(Min))
print(Max , a.count(Max))
