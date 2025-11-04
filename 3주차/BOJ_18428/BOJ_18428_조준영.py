import sys

input = sys.stdin.readline

from itertools import combinations

N = int(input().strip())

aisle, teacher, nostudent = [], [], []

r=0

def patrol(y,x):
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    i=0
    while i<4:
        dy,dx = direction[i]
        nx = x+dx
        ny = y+dy

        while 0<=nx<N and 0<=ny<N:
            if aisle[ny][nx] == "O":
                break
            if aisle[ny][nx]=="S":
                return True
            nx += dx
            ny += dy
        i+=1

    return False

def watch_all():
    j=0
    while j < len(teacher):
        ty, tx = teacher[j]
        if patrol(ty, tx):
            return False
        j+=1

    return True


while r<N:
    row = input().split()
    aisle.append(row)
    c=0
    while c<N:
        if row[c]=="T":
            teacher.append((r,c))
        elif row[c]=="X":
            nostudent.append((r,c))
        c+=1
    r+=1

ans = False
for o in combinations(nostudent, 3):
    i=0
    while i<3:
        y,x=o[i]
        aisle[y][x] = "O"
        i+=1
    
    if watch_all():
        print("YES")
        ans=True
        break
    
    j=0
    while j<3:
        y, x = o[j]
        aisle[y][x]="X"
        j+=1
if not ans:
    print("NO")