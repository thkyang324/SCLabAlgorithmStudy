import sys
from copy import deepcopy

input=lambda: sys.stdin.readline().strip()

def parse_input():
    N, M, H = map(int, input().split())
    milk_choco = list()
    home = None

    for i in range(N):
        line = input().split()
        for j in range(N):
            if line[j] == "1":
                home = (j, i)
            elif line[j] == "2":
                milk_choco.append((j, i))
    
    return N, M, H, milk_choco, home

def to_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1-x2) + abs(y1-y2)

def find_reachable_coords(cloc, hp, mclocs, visited):
    drinkable_mcs = []
    for mcloc in mclocs:
        if to_distance(cloc, mcloc) <= hp and not visited[mcloc]:
            drinkable_mcs.append(mcloc)
    return drinkable_mcs

def main():
    N, M, H, milk_choco, home = parse_input()
    MAX_CHOCO = len(milk_choco)
    mc2idx = {i:j for j, i in enumerate(milk_choco)}
    visited = {i: False for i in milk_choco}
    memo = {}

    def dfs(jw_loc, hp):
        visited_set = [False] * len((milk_choco))
        for k, v in visited.items():
            if v:
                visited_set[mc2idx[k]] = True

        key = (jw_loc, hp, tuple(visited_set))
        
        if key in memo:
            return memo[key]

        drinkable_mc_list = find_reachable_coords(jw_loc, hp, milk_choco, visited)
        can_go_home = to_distance(jw_loc, home) <= hp
        n_eaten = sum(visited.values())
        
        if len(drinkable_mc_list) == 0 or n_eaten == MAX_CHOCO:
            return n_eaten if can_go_home else 0

        answers = []
        for next_choco_loc in drinkable_mc_list:
            visited[next_choco_loc] = True
            answers.append(dfs(next_choco_loc, hp - to_distance(next_choco_loc, jw_loc) + H))
            visited[next_choco_loc] = False
        
        if can_go_home and jw_loc != home:
            answers.append(dfs(home, hp - to_distance(home, jw_loc)))

        ans = max(answers)
        memo[key] = ans
        return ans
    
    print(dfs(home, M))


if __name__ == "__main__":
    main()
    