input = __import__("sys").stdin.readline
from collections import deque

N, M = map(int, input().split())
sw = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    x, y, a, b = map(int, input().split())
    sw[x][y].append((a, b))

on = [[False] * (N + 1) for _ in range(N + 1)]
on[1][1] = True

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

while True:
    changed = False
    vis = [[False] * (N + 1) for _ in range(N + 1)]
    q = deque([(1, 1)])
    vis[1][1] = True

    while q:
        x, y = q.popleft()

        # 현재 방 ON
        for a, b in sw[x][y]:
            if not on[a][b]:
                on[a][b] = True
                changed = True
                # 방금 켠 방이 이미 방문한 방과 인접하면 큐 삽입
                for k in range(4):
                    na, nb = a + dx[k], b + dy[k]
                    if 1 <= na <= N and 1 <= nb <= N and vis[na][nb]:
                        if not vis[a][b]:
                            vis[a][b] = True
                            q.append((a, b))
                        break

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 1 <= nx <= N and 1 <= ny <= N and on[nx][ny] and not vis[nx][ny]:
                vis[nx][ny] = True
                q.append((nx, ny))

    if not changed:
        break

ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        ans += 1 if on[i][j] else 0
print(ans)
