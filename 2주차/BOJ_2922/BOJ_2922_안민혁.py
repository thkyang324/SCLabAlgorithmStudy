import sys
input = sys.stdin.readline

vowels = set("AEIOU")
s = list(input().strip())
n = len(s)

# 0=없음(초기),1=모음,2=자음
def typ(ch):
    return 1 if ch in vowels else 2

init_hasL = any(ch == 'L' for ch in s)

# dp[last2][last1][hasL] = count

dp = [[[0]*2 for _ in range(3)] for __ in range(3)]
dp[0][0][1 if init_hasL else 0] = 1

for i in range(n):
    ndp = [[[0]*2 for _ in range(3)] for __ in range(3)]
    ch = s[i]
    for l2 in range(3):
        for l1 in range(3):
            for hasL in (0,1):
                cur = dp[l2][l1][hasL]
                if cur == 0:
                    continue
                if ch != '_':
                    t = typ(ch)
                    if not (l2 == l1 == t and l2 != 0):
                        nh = hasL or (ch == 'L')
                        ndp[l1][t][1 if nh else 0] += cur
                else:
                    t = 1
                    if not (l2 == l1 == t and l2 != 0):
                        ndp[l1][t][hasL] += cur * 5
                        
                    t = 2
                    if not (l2 == l1 == t and l2 != 0):
                        ndp[l1][t][1] += cur
                        
                    if not (l2 == l1 == 2 and l2 != 0):
                        ndp[l1][2][hasL] += cur * 20
    dp = ndp

ans = 0
for l2 in range(3):
    for l1 in range(3):
        ans += dp[l2][l1][1]
sys.stdout.write(str(ans))
