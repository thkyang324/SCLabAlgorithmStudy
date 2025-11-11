import sys
input = sys.stdin.readline

# 재귀 + 지문대로 구현

def rot(idx, direction, parent):
    gear_left = gear[idx][6]
    gear_right = gear[idx][2]

    if direction == 1: # 시계방향
        gear[idx] = [gear[idx][-1]] + gear[idx][:-1]
        next_direction = -1
    else: # 반시계
        gear[idx] = gear[idx][1:] + [gear[idx][0]]
        next_direction = 1

    if idx > 0 and idx-1 != parent and gear[idx-1][2] != gear_left:
        rot(idx-1, next_direction, idx)     
    if idx < 3 and idx+1 != parent and gear[idx+1][6] != gear_right:
        rot(idx+1, next_direction, idx)    

gear = []

for i in range(4):
    gear.append(list(map(int, list(input().strip()))))

K = int(input())

for k in range(K):
    state = [False] * 4
    target_i, direction = map(int, input().split())
    target_i -=1
    state[target_i] = True
    rot(target_i, direction, target_i)

score = 0
if gear[0][0] == 1:
    score+=1
if gear[1][0] == 1:
    score+=2
if gear[2][0] == 1:
    score+=4
if gear[3][0] == 1:
    score+=8

sys.stdout.write(str(score))