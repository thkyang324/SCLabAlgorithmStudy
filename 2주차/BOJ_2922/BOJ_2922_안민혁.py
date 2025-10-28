import sys
from collections import deque, Counter
input = sys.stdin.readline

# 즐거운 단어: 모음(A,E,I,O,U) 3개 연속 X, 자음(나머지 알파벳) 3개 연속 X, L을 반드시 포함

vowels = ['A','E','I','O','U','!']
consonants = [chr(i) for i in range(65, 91) if chr(i) not in vowels]

given_word = list(input().strip())
n_words = len(given_word)

n_vowels = len(vowels) # 5
n_consonants = len(consonants) # 21
# total = 26

idx_blank = []
for i, word in enumerate(given_word):
    if word == '_':
        idx_blank.append(i)
n_blank = len(idx_blank)
idx_blank += [0]

def check_slide(word, cur_idx):
    n = len(word)
    start = max(0, cur_idx - 2)
    end = min(cur_idx, n - 3)
    for s in range(start, end + 1):
        a, b, c = word[s], word[s + 1], word[s + 2]
        if a == '_' or b == '_' or c == '_':
            continue
        ai = a in vowels
        bi = b in vowels
        ci = c in vowels 
        if ai == bi == ci:
            return False
    return True

def check(word):
    count = 0
    v = 0
    c = 0
    counter = dict(Counter(word))
    if '!' in counter:
        v = counter['!']
    if '@' in counter:
        c = counter['@']
        
    if 'L' in counter:
        count = 5**v * 21**c
    else: # L 없음
        if c == 0:
            return 0
        else:
            count = 5**v * (21**c - 20**c)

    return count


def dfs(idx,depth, word):
    count = 0
    queue = deque()
    queue.append((idx, depth, word))

    while queue:
        cur_idx, cur_depth, cur_word = queue.pop()
        if cur_depth == n_blank:
            # cur_word 형식: [L, @, V] [L, !, V], [V, !, @, K] 등
            count += check(cur_word) 
        else:
            next_depth = cur_depth + 1 
            # 모음
            next_word = cur_word.copy()
            next_word[cur_idx] = '!'
            if check_slide(next_word, cur_idx):                
                queue.append((idx_blank[next_depth], next_depth, next_word))

            # 자음
            next_word = cur_word.copy()
            next_word[cur_idx] = '@'
            if check_slide(next_word, cur_idx):                
                queue.append((idx_blank[next_depth], next_depth, next_word))



    return count

sys.stdout.write(str(dfs(idx_blank[0],0, given_word)))

    



