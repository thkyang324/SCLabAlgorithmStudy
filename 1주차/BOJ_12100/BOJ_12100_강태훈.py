import sys
from copy import deepcopy

input=sys.stdin.readline

def show_arr(arr):
    print("*"*100)
    for line in arr:
        print(line)
    print()

def parse_input():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().strip().split())))
    
    return N, board

def rot90(arr):
    return [list(i[::-1]) for i in zip(*arr)]

def rot270(arr):
    return [list(i) for i in zip(*arr)][::-1]

def rot180(arr):
    return [list(i[::-1]) for i in arr[::-1]]


def fill_zero(line, N):
    while len(line) < N:
        line.append(0)
    return line

def move_left(arr):
    N = len(arr)
    new_arr = []
    for line in arr:
        new_line = []
        flag = True
        for i in range(N):
            push_target = line[i]
            if push_target == 0:
                continue
            elif len(new_line) > 0 and new_line[-1] == push_target and flag:
                new_line[-1] *= 2
                flag = False
            else:
                new_line.append(push_target)
                flag=True
        new_arr.append(fill_zero(new_line, N))
    return new_arr

move_fn_list = [
    [move_left],
    [rot90, move_left, rot270],
    [rot180, move_left, rot180],
    [rot270, move_left, rot90],
]

def reduce_fn_list(board, fn_list):
    for fn in fn_list:
        board = fn(board)
    return board

def main():
    _, input_board = parse_input()

    def dfs(cnt, board):
        board = deepcopy(board)
        if cnt == 5:
            return max(map(max, board))
        return max([dfs(cnt+1, reduce_fn_list(board, move_fn_list[i])) for i in range(4)])
    
    print(dfs(0, input_board))

if __name__ == "__main__":
    main()

"""
TC 1: 
3
2 2 2
4 4 4
8 8 8
"""
