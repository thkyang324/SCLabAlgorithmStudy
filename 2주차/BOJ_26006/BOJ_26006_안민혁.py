import sys
input = sys.stdin.readline

# 아이디어: king 주변 9칸 검사

# 1. 처음에 체스판 2d array 만들었으나 타임아웃 -> 앞으로 N 확인 해야할 듯
# 2. 대각선 검사를 브루트포스로 함 -> 타임아웃 
#     -> r+c 또는 r-c 같으면 동일 대각선상에 있는거 이용해서 해결

# ps: 원소 포함 확인할 때 set이 O(1)이라 빠르다고 함


# 0 1 2 / 3 4 5 / 6 7 8
dr = [-1, -1, -1,  0, 0, 0,  1, 1, 1] 
dc = [-1,  0,  1, -1, 0, 1, -1, 0, 1]

N, numQ = map(int, input().split())
kingR, kingC = map(int, input().split())

queens = []
row_has_q = set()
col_has_q = set()
diag1_has_q = set()  # r - c
diag2_has_q = set()  # r + c
occupied = set()

for _ in range(numQ):
    r, c = map(int, input().split())
    queens.append((r, c))
    occupied.add((r, c))
    row_has_q.add(r)
    col_has_q.add(c)
    diag1_has_q.add(r - c)
    diag2_has_q.add(r + c)

def onboard(r, c):
    return 1 <= r <= N and 1 <= c <= N

def attacked(r, c): 
    return (r in row_has_q) or (c in col_has_q) or ((r - c) in diag1_has_q) or ((r + c) in diag2_has_q)

state = [0] * 9

for i in range(9):
    r = kingR + dr[i]
    c = kingC + dc[i]

    if i == 4:
        # 킹이 공격받는지
        state[4] = 1 if attacked(kingR, kingC) else 0
        continue

    # 주변: 보드 밖이거나, 퀸이 있거나, 해당 칸이 공격받으면 state =1 
    if (not onboard(r, c)) or ((r, c) in occupied) or attacked(r, c):
        state[i] = 1
    else:
        state[i] = 0

state_sum = sum(state)

if state[4] == 0:
    res = 'STALEMATE' if state_sum == 8 else 'NONE'
else:
    res = 'CHECKMATE' if state_sum == 9 else 'CHECK'

sys.stdout.write(res)
