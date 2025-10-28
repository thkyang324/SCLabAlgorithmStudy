import sys

input=sys.stdin.readline


VOWEL = set(list("AEIOU"))
CONS_no_L = set(list("BCDFGHJKMNPQRSTVWXYZ"))


def encode(x):
    encoded = []
    under_bar_indexs = []
    has_L = False
    for idx in range(len(x)):
        i = x[idx]
        if i == "_" :
            encoded.append(0)
            under_bar_indexs.append(idx)
        elif i in VOWEL :
            encoded.append(1)
        elif i in CONS_no_L :
            encoded.append(2)
        elif i == "L":
            encoded.append(3)
            has_L = True
        else:
            -1
    return encoded, under_bar_indexs, has_L


def is_vowel(t):
    return t == 1

def is_cons(t):
    return t in (2, 3)


def parse_input():
    return input().strip().upper()


def main():
    word = parse_input()
    encoded, udb_idxs, has_L = encode(word)
    n = len(encoded)
    
    def check(idx):
        for start in range(idx - 2, idx + 1):
            if start < 0 or start + 2 >= n:
                continue
            a, b, c = encoded[start:start+3]
            if 0 in (a, b, c):
                continue
            if is_vowel(a) and is_vowel(b) and is_vowel(c):
                return True
            if is_cons(a) and is_cons(b) and is_cons(c):
                return True
        return False

    def btk(k, has_L_flag):
        if k == len(udb_idxs):
            return 1 if has_L_flag else 0
        cur_index = udb_idxs[k]
        total = 0

        encoded[cur_index] = 1
        if not check(cur_index):
            total += 5 * btk(k + 1, has_L_flag)

        encoded[cur_index] = 2
        if not check(cur_index):
            total += 20 * btk(k + 1, has_L_flag)

        encoded[cur_index] = 3
        if not check(cur_index):
            total += 1 * btk(k + 1, True)

        encoded[cur_index] = 0
        return total
    
    print(btk(0, has_L))


if __name__ == "__main__":
    main()