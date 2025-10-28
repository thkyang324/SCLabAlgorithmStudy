import sys

input=sys.stdin.readline

def parse_input():
    N, K = map(int, input().split())
    R, C = map(int, input().split())
    bqs = []
    for _ in range(K):
        Ri, Ci = map(int, input().split())
        bqs.append((Ri, Ci))

    return (
        (N, K), (R, C), bqs
    )

def check_check(K, Qs):
    for Q in Qs:
        if any([
            K[0] == Q[0],
            K[1] == Q[1],
            abs(K[0]-Q[0]) == abs(K[1]-Q[1])
        ]):
            return True
    return False
        


def main():
    (N, K), (R, C), bqs = parse_input()

    # print(
    #     "{} x {} Board, N-Queens = {}".format(N, N, K), 
    #     "White King if located in ({}, {})".format(R, C), 
    #     *["\t Black Queen(i={}) if located in ({}, {})".format(i, *bqs[i]) for i in range(K)], 
    # sep="\n")

    is_check = check_check((R, C), bqs)
    can_move = False
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        nr, nc = R+dr, C+dc
        if any([nr==0, nc==0, nr>N, nc>N]):
            continue
        if not check_check((nr, nc), bqs):
            can_move = True
            break
    
    if is_check and can_move:
        print("CHECK")
    elif is_check and not can_move:
        print("CHECKMATE")
    elif not is_check and not can_move:
        print("STALEMATE")
    else:
        print("NONE")


if __name__ == "__main__":
    main()