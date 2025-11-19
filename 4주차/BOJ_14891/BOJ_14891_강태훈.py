# 단순 시뮬레이션 버전
import sys
input = sys.stdin.readline

def parse_input():
    wheels = [list(map(int, list(input().strip()))) for _ in range(4)]
    K = int(input())
    cmds = [list(map(int, input().strip().split())) for _ in range(K)]
    return wheels, cmds

def main():
    wheels, cmds = parse_input()
    for i in range(len(cmds)):
        w_idx = cmds[i][0] - 1
        rot_dirs = [0] * 4
        rot_dirs[w_idx] = cmds[i][1]
        for r_idx in range(w_idx+1, 4):
            if wheels[r_idx-1][2] == wheels[r_idx][6]:
                break
            rot_dirs[r_idx] = -rot_dirs[r_idx-1]
        
        for l_idx in range(w_idx-1, -1, -1):
            if wheels[l_idx+1][6] == wheels[l_idx][2]:
                break
            rot_dirs[l_idx] = -rot_dirs[l_idx+1]

        for j in range(4):
            if rot_dirs[j] == 1:
                wheels[j] = [wheels[j][-1]] + wheels[j][:-1]
            elif rot_dirs[j] == -1:
                wheels[j] = wheels[j][1:] + [wheels[j][0]]

    a, b, c, d = list(zip(*wheels))[0]
    print(a+2*b+4*c+8*d)



if __name__ == "__main__":
    main()

# 포인터 조정 버전
"""
import sys
input = sys.stdin.readline

def main():
    wheels = [list(map(int, list(input().strip()))) for _ in range(4)]
    K = int(input().strip())
    cmds = [tuple(map(int, input().split())) for _ in range(K)]

    pos = [0, 0, 0, 0]

    for num, d in cmds:
        idx = num - 1
        rot = [0] * 4
        rot[idx] = d

        orig_pos = pos.copy()

        for i in range(idx+1, 4):
            left = wheels[i-1][(orig_pos[i-1] + 2) % 8]
            right = wheels[i][(orig_pos[i] + 6) % 8]
            if left != right:
                rot[i] = -rot[i-1]
            else:
                break

        for i in range(idx-1, -1, -1):
            right = wheels[i+1][(orig_pos[i+1] + 6) % 8]
            left = wheels[i][(orig_pos[i] + 2) % 8]
            if left != right:
                rot[i] = -rot[i+1]
            else:
                break

        for i in range(4):
            if rot[i] == 1:
                pos[i] = (pos[i] - 1) % 8
            elif rot[i] == -1:
                pos[i] = (pos[i] + 1) % 8

    score = wheels[0][pos[0]] * 1 + wheels[1][pos[1]] * 2 + wheels[2][pos[2]] * 4 + wheels[3][pos[3]] * 8
    print(score)

if __name__ == "__main__":
    main()
"""