import sys
input = sys.stdin.readline

N = int(input().strip())
top_n_num = list(map(int, input().split()))

def mixing(N, K):
    orig_index = list(range(N))
    bottom_len = 1<< K
    bottom = orig_index[-bottom_len:]
    other = orig_index[:-bottom_len]
    orig_index = bottom + other

    prev_length = bottom_len


    for j in range(K-1, -1, -1):
        count = 1<<j
        pre = orig_index[:prev_length-count]
        post = orig_index[prev_length-count:prev_length]
        rest = orig_index[prev_length:]
        orig_index= post+pre+rest
        prev_length= count

    p=[0]*N
    for new, old in enumerate(orig_index):
        p[old]=new
    return p

T=[0]*N
for new, card in enumerate(top_n_num):
    orig_index= card-1
    T[orig_index]=new

ks=[]
k=1
while (1<<k) < N:
    ks.append(k)
    k+=1

# min_k=1
# max_k = (N-1)//2
mix_k={}
k_mix={}

for K in ks:
    mk=mixing(N,K)
    mix_k[K]= mk
    k_mix[tuple(mk)]=K
# for K in range(min_k, max_k+1):
#     mk=mixing(N,K)
#     mix_k[K]=mk
#     k_mix[tuple(mk)]=K

def counter_mix(p):
    N = len(p)
    mix = [0]*N
    for x in range(N):
        mix[p[x]]=x
    return mix

def add_mix(x,y):
    N=len(x)
    c = [0]*N
    for z in range(N):
        c[z]=x[y[z]]
    return c

ans_k1, ans_k2 = None, None

for k1 in ks:
    mix1 = mix_k[k1]
    counter_mix1 = counter_mix(mix1)
    mix2_need = add_mix(T, counter_mix1)
    key = tuple(mix2_need)
    if key in k_mix:
        ans_k1=k1
        ans_k2=k_mix[key]
        break

print(ans_k1, ans_k2)