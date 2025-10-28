from collections import deque
import sys
input = sys.stdin.readline

sample ='''
3 7
1 1 1 2
2 1 2 2
1 1 1 3
2 3 3 1
1 3 1 2
1 3 2 1
1 1 3 3
answer = 5
'''

sample2='''
4 10
1 1 1 2
1 2 1 3
1 2 4 1
1 3 1 4
1 3 3 1
1 4 2 4
1 4 2 1
2 1 4 4
3 1 4 3
4 1 3 4
answer = 11
'''

sample3='''
4 10
1 1 1 2
1 2 4 1
1 2 1 3
1 3 3 1
1 3 1 4
1 4 2 4
1 4 2 1
2 1 4 4
3 1 4 3
4 1 3 4
answer = 11
'''

sample4='''
5 14
1 2 3 4
1 2 3 2
1 2 3 3
1 3 4 3
1 4 5 3
1 4 5 4
1 4 5 5
1 1 1 2
1 2 1 3
1 3 1 4
1 4 1 5
1 4 2 1
2 1 4 1
2 1 4 2
answer = 15
'''

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M = map(int, input().split())

graph = {}

for i in range(M):
    x, y, a, b = map(int, input().split())
    if (x, y) not in graph:
        graph[(x, y)] = []
    graph[(x, y)].append((a, b))

light_on = [[0] * (N+1) for _ in range(N+1)]
connected = [[0] * (N+1) for _ in range(N+1)]
visited = [[0] * (N+1) for _ in range(N+1)]

def search(start_x, start_y):
    # count = 1
    queue = deque()
    queue.append((start_x, start_y)) 
    light_on[start_x][start_y] = 1
    visited[start_x][start_y] = 1
    

    while queue:
        x, y = queue.popleft() 

        if (x, y) not in graph: # 현재 방에서 switch 체크
            pass
        else: # 스위치 있으면 불켜기
            while graph[(x, y)]:
                a, b = graph[(x, y)].pop() 
                light_on[a][b] = 1
                    
                # 불켜진 방으로 갈 수 있는지 체크
                for i in range(4):
                    nx = a + dx[i]
                    ny = b + dy[i]
                    if 1<= nx <= N and 1 <= ny <= N and visited[nx][ny] == 1:
                        visited[a][b] = 1 # 이동가능한 방, 큐에 넣음
                        queue.append((a, b))
                        break

        # 방 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1<= nx <= N and 1 <= ny <= N and light_on[nx][ny] == 1 and visited[nx][ny] == 0: 
                visited[nx][ny] = 1
                queue.append((nx, ny))

    return light_on # 갈 수 있는 방을 세는게 아니라 스위치 켜지는 방을 세는 거였음.. 이거 하나 때문에 디버깅 5시간 함.. 문제를 잘 읽자

light_on = search(1, 1)
res = 0
for i in range(len(light_on)):
    res+= sum(light_on[i])
sys.stdout.write(str(res))