dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input=__import__("sys").stdin.readline

N = int(input())
board = [list(input().strip().split()) for _ in range(N)]
S_positions = [(i, j) for i in range(N) for j in range(N) if board[i][j] == 'S']
ans = "NO"
teachers = []
empties = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            teachers.append((i, j))
        elif board[i][j] == 'X':
            empties.append((i, j))

def is_hide():
    for x, y in teachers:
        for d in range(4):
            nx, ny = x, y
            while True:
                nx += dx[d]
                ny += dy[d]
                # 범위 벗어나면 pass
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break
                # 장애물 만나면 pass
                if board[nx][ny] == 'O':
                    break
                # 학생 보이면 GG
                if board[nx][ny] == 'S':
                    return False
    return True

def backtracking(idx, cnt):
    global ans
    if ans == "YES":
        return
    
    if cnt == 3:
        if is_hide():
            ans = "YES"
        return
    
    if idx == len(empties):
        return
    
    x, y = empties[idx]

    board[x][y] = 'O'
    backtracking(idx + 1, cnt + 1) # 장애물 놓아보기
    board[x][y] = 'X'

    backtracking(idx + 1, cnt) # 장애물 안놓고 pass

    return 

backtracking(0, 0)
print(ans)