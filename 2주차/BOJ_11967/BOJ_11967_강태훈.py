import sys
from collections import deque

input=sys.stdin.readline

def show_arr(arr):
    print("*"*100)
    for line in arr:
        print(line)
    print()

def parse_input():
    N, M = map(int, input().split())
    board = [[[] for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        x, y, a, b = map(int, input().split())
        board[x][y].append((a, b))
        
    return N, M, board

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def main():
    N, _, board = parse_input()
    queue = deque([(1, 1)])
    visited = [[False] * (N+1) for _ in range(N+1)]
    light = [[False] * (N+1) for _ in range(N+1)]
    visited[1][1] = True
    light[1][1] = True

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        while board[x][y]:
            bx, by = board[x][y].pop()
            light[bx][by] = True
            for dir in range(4):
                nx2 = bx + dx[dir]
                ny2 = by + dy[dir]
                if 1 <= nx2 <= N and 1 <= ny2 <= N and visited[nx2][ny2]:
                    queue.append((bx, by))
                    visited[bx][by] = True
                    break
        
        for didx in range(4):
            nx = x + dx[didx]
            ny = y + dy[didx]

            if 1 <= nx <= N and 1 <= ny <= N and light[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
            

    # show_arr(board)
    # show_arr(visited)
    # show_arr(light)
    print(sum(sum(light, [])))

if __name__ == "__main__":
    main()
"""
"""