# 2^K개의 카드를 더미의 맨 위로 올린다.
# i(2 ≤ i ≤ K + 1)번째 단계는 직전에 맨 위로 올린 카드 중 밑에서 2^(K - i + 1)개의 카드를 더미의 맨 위로 올린다.

input=__import__("sys").stdin.readline

N = int(input())
C = list(map(int, input().split()))

def shuffle(L, k):
    n = len(L)

    cnt = 2**k

    L = L[n- cnt:] + L[:n - cnt]
    prev_cnt = cnt

    for step in range(2, k+2):
        cnt //= 2

        prev = L[:prev_cnt]
        rest = L[prev_cnt:]

        cur = prev[prev_cnt - cnt:]
        cur_rest = prev[:prev_cnt - cnt]

        L = cur + cur_rest + rest

        prev_cnt = cnt
    
    return L

def solve(ans):
    for k1 in range(1, 10):
        first = shuffle(list(range(1, N+1)), k1)
        for k2 in range(1, 10):
            second = shuffle(first, k2)
            if second == ans:
                print(k1, k2)
                __import__("sys").exit(0)

solve(C)