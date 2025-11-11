import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, H, D = map(int, input().split())

def bfs(sr,sc, hp, v, m):
    q = deque()
    v[sr][sc] = hp
    q.append((sr,sc, hp, 0, 0))

    while q:
        cr, cc, chp, cd, cstep = q.popleft()
        # print(cr, cc, chp, cd, cstep, m[cr][cc])
        if m[cr][cc] == 'E':
            return cstep
        if m[cr][cc] == 'U':
            cd = D
        if m[cr][cc] != 'S':
            if cd > 0:
                cd-=1
            else:
                chp-=1

        if chp > 0:
            for i in range(4):
                nr, nc = cr + dr[i], cc + dc[i] 
                if 0<=nr<N and 0<=nc<N and v[nr][nc] < cd + chp:

                    v[nr][nc] = cd + chp
                    q.append((nr,nc, chp, cd, cstep+1))
    return -1

m = [[""] * N for _ in range(N)]
v = [[-1] * N for _ in range(N)] 
for r in range(N):
    # U, S, E, .
    m[r] = list(input().strip())

for r in range(N):
    for c in range(N):
        if m[r][c] == 'S':
            step = bfs(r,c, H, v, m)
            sys.stdout.write(str(step))
            exit(0)