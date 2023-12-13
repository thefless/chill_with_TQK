from array import *

n , q = map(int , input().split())

st = array('i' , [0] * (4 * (n + 1)))
lazy = array('i' , [0] * (4 * (n + 1)))

def down(id , l , r):
    if lazy[id] == 0 or l == r: return
    k = lazy[id]
    lazy[id] = 0
    st[id << 1] += k
    lazy[id << 1] += k
    st[id << 1 | 1] += k
    lazy[id << 1 | 1] += k
def update(id , l , r , u , v , val):
    if l > v or r < u:
        return
    if u <= l and r <= v:
        lazy[id] += val
        st[id] += val
        down(id , l , r)
        return; 
    mid = l + r >> 1
    down(id , l , r)
    update(id << 1 , l , mid , u , v , val)
    update(id << 1 | 1 , mid + 1 , r , u , v , val)
    st[id] = max(st[id << 1] , st[id << 1 | 1])

for i in range(q):
    a , b , k = map(int , input().split())
    update(1 , 1 , n , a , b , k)

print(st[1])