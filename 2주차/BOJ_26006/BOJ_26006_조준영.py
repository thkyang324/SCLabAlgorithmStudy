import sys

input = sys.stdin.readline

N, K = map(int, input().split())
R,C = map(int, input().split())

queen = []
i=0
while i<K:
    r, c = map(int, input().split())
    queen.append((r,c))
    i+=1

go = []
go.append((-1,-1)); go.append((-1,0)); go.append((-1,1))
go.append((1,-1)); go.append((1,0)); go.append((1,1))
go.append((0,-1)); go.append((0,1))

def ckattk(rr,cc):
    j= 0
    while j < K:
        qr, qc = queen[j]
        if qr == rr:
            return True
        if qc == cc:
            return True
        dr = qr - rr
        dc = qc -cc
        if dr < 0:
            adr = -dr
        else:
            adr = dr

        if dc < 0:
            adc = -dc
        else:
            adc= dc

        if adr == adc:
            return True
        j+=1
    return False

chk = ckattk(R,C)

king = False

t=0
while t<8:
    dx, dy = go[t]
    nr = R+dx
    nc = C+dy

    if 1<=nr<=N and 1 <= nc <= N:
        if not ckattk(nr, nc):
            king = True
            break
    t+=1

if chk and king:
        print("CHECK")
elif chk and not king:
    print("CHECKMATE")
elif (not chk) and (not king):
    print("STALEMATE")
else:
    print("NONE")