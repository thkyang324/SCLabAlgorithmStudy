input = __import__("sys").stdin.readline

S = input().strip()
VOW = set("AEIOU")

answers = []

def backtracking(idx, cv, cc, hasL, ways):
    if cv >= 3 or cc >= 3:
        return
    if idx == len(S):
        if hasL:
            answers.append(ways)
        return

    ch = S[idx]
    if ch == "_":
        # 모음 채우기 (5가지)
        backtracking(idx + 1, cv + 1, 0, hasL, ways * 5)
        # L 채우기 (1가지, 자음)
        backtracking(idx + 1, 0, cc + 1, True, ways * 1)
        # L을 제외한 자음 채우기 (20가지)
        backtracking(idx + 1, 0, cc + 1, hasL, ways * 20)
    else:
        if ch in VOW:
            backtracking(idx + 1, cv + 1, 0, hasL, ways)
        else:
            backtracking(idx + 1, 0, cc + 1, hasL or (ch == "L"), ways)

backtracking(0, 0, 0, False, 1)
print(sum(answers))
