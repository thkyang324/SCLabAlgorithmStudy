import sys
input = sys.stdin.readline

N = int(input())
lst =  [[] for _ in range(N)]

for _ in range(N-1):
    p, q, w = input().split()
    p = int(p)
    q = int(q)
    w = int(w)
    lst[p].append((q,w))
    lst[q].append((p,w))
    
def dia(start):
    stack = [(start, -1, 0)]
    length = [-1]*N
    length[start]=0
    order = []
    while stack:
        v,q,d = stack.pop()
        order.append(v)
        for nv, w in lst[v]:
            if nv == q:
                continue
            if length[nv] == -1:
                length[nv] = d+w
                stack.append((nv, v, d+w))

        
    u = max(range(N), key=lambda x: length[x])
    return u, length

u, _ = dia(0)
v, dis_u = dia(u)
w_dia =  max(dis_u)

parant = [-1]*N
parent_ew = [0]*N
order = []

stack =[0]
parant[0]=-2
while stack:
    x = stack.pop()
    order.append(x)
    for nx, w in lst[x]:
        if parant[nx] != -1:
            continue
        parant[nx]=x
        parent_ew[nx] = w
        stack.append(nx)
    
parant[0] = -1

con = [len(lst[i]) for i in range(N)]
leaf = [con[i]==1 for i in range(N)]

down = [None]*N
up = [None]*N
up[0] = None

for x in reversed(order):
    if leaf[x]:
        down[x]=0
    else:
        best = None
        for nx, w in lst[x]:
            if nx == parant[x]:
                continue
            if down[nx] is not None:
                dep = w + down[nx]
                if best is None or dep <best:
                    best = dep
        if best is None and leaf[x]:
            down[x]=0
        else:
            down[x]=best
            
for x in order:
    child = []
    for nx, w in lst[x]:
        if nx == parant[x]:
            continue
        if down[nx] is not None:
            child.append((w+down[nx],nx))
    child.sort()
    min_a = child[0] if len(child)>0 else (None,-1)

    min_b = child[1] if len(child)>1 else (None,-1)
    
    leaf_self = 0 if leaf[x] else None
    parent_dir = up[x]
    
    for nx, w in lst[x]:
        if nx == parant[x]:
            continue
        best_other = None
        
        if parent_dir is not None:
            best_other = parent_dir
        if leaf_self is not None:
            if best_other is None or leaf_self<best_other:
                best_other = leaf_self
        min_other = min_a[0] if min_a[1]!=nx else min_b[0]
        if min_other is not None:
            if best_other is None or min_other < best_other:
                best_other = min_other
                
        if best_other is not None:
            up[nx] = w + best_other
        else:
            up[nx] = None 
min_leaf_dis = None

for x in range(N):
    opt = []
    if up[x] is not None:
        opt.append(up[x])
    
    for nx, w in lst[x]:
        if nx == parant[x]:
            continue
        if down[nx] is not None:
            opt.append(w+down[nx])
            
    if leaf[x]:
        opt.append(0)
        
    if len(opt)>=2:
        opt.sort()
        s= opt[0]+opt[1]
        if min_leaf_dis is None or s < min_leaf_dis:
            min_leaf_dis=s
                
print(w_dia)
print(min_leaf_dis)              