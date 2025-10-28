import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

sw = [[[] for _ in range(n + 1)] for __ in range(n + 1)]

for _ in range(m):
    x,y,a,b = map(int, input().split())
    sw[x][y].append((a,b))

light = []
for _ in range(n+1):
    row= []
    for __ in range(n+1):
        row.append(False)
    light.append(row)

vs = []
for _ in range(n+1):
    row=[]
    for __ in range(n+1):
        row.append(False)
    vs.append(row)

light[1][1] = True
vs[1][1] = True
final = 1

q =  deque()
q.append((1,1))

dirs=[(1,0),(-1,0),(0,1),(0,-1)]

while q:
    x,y = q.popleft()

    for a,b in sw[x][y]:
        if not light[a][b]:
            light[a][b]=True
            final += 1

            can = False
            for dx, dy in dirs:
                na = a + dx
                nb= b+ dy
                if 1<=na<=n and 1<=nb<=n:
                    if vs[na][nb]:
                        can =True
                        break
            
            if can and not vs[a][b]:
                vs[a][b] = True
                q.append((a,b))

    for dx, dy in dirs:
        nx = x + dx
        ny = y+ dy
        if 1<=nx<=n and 1<= ny <=n:
            if light[nx][ny] and not vs[nx][ny]:
                vs[nx][ny] = True
                q.append((nx,ny))
print(final)