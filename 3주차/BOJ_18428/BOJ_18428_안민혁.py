import sys
from itertools import combinations
input = sys.stdin.readline

# O 들어갈 자리 + check 완탐

N = int(input())
aisle = [input().split() for _ in range(N)]


teachers = []
empties = []

for r in range(N):
    for c in range(N):
        if aisle[r][c] == "T":
            teachers.append((r, c))
        elif aisle[r][c] == "X":
            empties.append((r, c))

def check():
    for r, c in teachers:
        # 상
        nr = r - 1
        while nr >= 0:
            if aisle[nr][c] == "O":
                break
            if aisle[nr][c] == "S":
                return True
            nr -= 1
        # 하
        nr = r + 1
        while nr < N:
            if aisle[nr][c] == "O":
                break
            if aisle[nr][c] == "S":
                return True
            nr += 1
        # 좌
        nc = c - 1
        while nc >= 0:
            if aisle[r][nc] == "O":
                break
            if aisle[r][nc] == "S":
                return True
            nc -= 1
        # 우
        nc = c + 1
        while nc < N:
            if aisle[r][nc] == "O":
                break
            if aisle[r][nc] == "S":
                return True
            nc += 1
    return False

answer = "NO"
for comb in combinations(empties, 3):
    for r, c in comb:
        aisle[r][c] = "O"
    if not check():
        answer = "YES"
        break
    # 초기화
    for r, c in comb:
        aisle[r][c] = "X"

print(answer)