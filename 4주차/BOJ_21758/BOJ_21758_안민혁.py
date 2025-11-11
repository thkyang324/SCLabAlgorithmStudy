import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))

S = [0]*N
for i in range(N):
    if i==0:
        S[i] = H[0]
    else:
        S[i] = S[i-1] + H[i]

max_honey = 0

for i in range(1, N-1):
    max_honey = max(max_honey, S[-1] - H[0] - H[i] + (S[-1] - S[i]))
    max_honey = max(max_honey, S[-1] - H[-1] - H[i] + S[i-1]) 
    max_honey = max(max_honey, S[i] - H[0] + (S[-1] - S[i-1] - H[-1])) 

sys.stdout.write(str(max_honey))