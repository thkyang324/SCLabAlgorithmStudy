import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
N = int(input())
curves = []
def get_pivot(curves):
    pivot = curves[-1]
    return pivot[0], pivot[1]

def rot90(px, py, curves):
    rotated = []
    for i in range(len(curves)-2, -1,-1):
        cx, cy  = curves[i][0], curves[i][1]
        dx = px-cx
        dy = py-cy
        if dx > 0:
            y = py - dx
        else:
            y = py + abs(dx)
        if dy > 0:
            x = px + dy
        else:
            x = px - abs(dy)
        rotated.append([x,y])
    return curves+rotated

all_curves = []
for i in range(N):
    x, y, d, g = map(int, input().split())
    curves = [[x,y], [x+dx[d], y+dy[d]]] # 0세대
    # 1세대 이상
    for i in range(1, g+1):
        px,py = get_pivot(curves)
        curves = rot90(px,py, curves)    
    all_curves += curves
all_curves = set(list(map(tuple, all_curves)))

count=0
for x, y in all_curves:
    if (x+1, y) in all_curves and (x, y+1) in all_curves and (x+1,y+1) in all_curves:
        count+=1
sys.stdout.write(str(count))