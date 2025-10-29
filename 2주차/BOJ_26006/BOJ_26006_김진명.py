input = __import__("sys").stdin.readline

N, K = map(int, input().split())
r0, c0 = map(int, input().split())

rows, cols, d1, d2 = set(), set(), set(), set()
for _ in range(K):
    r, c = map(int, input().split())
    rows.add(r)
    cols.add(c)
    d1.add(r - c)
    d2.add(r + c)

def attacked(r, c):
    return (r in rows) or (c in cols) or ((r - c) in d1) or ((r + c) in d2)

in_check = attacked(r0, c0)

legal = 0
for dr in (-1, 0, 1):
    for dc in (-1, 0, 1):
        if dr == 0 and dc == 0:
            continue
        nr, nc = r0 + dr, c0 + dc
        if 1 <= nr <= N and 1 <= nc <= N and not attacked(nr, nc):
            legal += 1

if in_check and legal > 0:
    print("CHECK")
elif in_check and legal == 0:
    print("CHECKMATE")
elif (not in_check) and legal == 0:
    print("STALEMATE")
else:
    print("NONE")
