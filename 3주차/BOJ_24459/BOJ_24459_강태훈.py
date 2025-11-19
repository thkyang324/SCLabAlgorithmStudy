import sys, heapq
input = sys.stdin.readline
INF = 10**18

def compress_tree(n, adj):
    deg = [len(adj[i]) for i in range(n)]
    keep = [i for i in range(n) if deg[i] != 2]
    new_id = [-1]*n

    for i,u in enumerate(keep):
        new_id[u]=i

    m = len(keep)
    if m == 0:
        return 1, [[(0,0)]]

    cadj = [[] for _ in range(m)]

    seen = set()

    for u in keep:
        uid = new_id[u]
        for v,w in adj[u]:
            if new_id[v] != -1:
                vid = new_id[v]
                if uid < vid and (uid,vid) not in seen:
                    cadj[uid].append((vid,w))
                    cadj[vid].append((uid,w))
                    seen.add((uid,vid))
                continue

            total = w
            prev = u
            cur = v

            while len(adj[cur]) == 2:
                a, wa = adj[cur][0]; b, wb = adj[cur][1]
                if a == prev: 
                    nxt, wn = b, wb
                else: 
                    nxt, wn = a, wa
                total += wn; prev, cur = cur, nxt

            vid = new_id[cur]
            if vid is None or vid == -1: 
                continue
            a,b = min(uid,vid), max(uid,vid)
            if (a,b) in seen: 
                continue
            seen.add((a,b))
            cadj[uid].append((vid,total)); cadj[vid].append((uid,total))
    return m, cadj

def dijkstra_furthest(s, n, adj):
    dist = [INF]*n; dist[s]=0; pq=[(0,s)]
    while pq:
        d,u = heapq.heappop(pq)
        if d!=dist[u]: 
            continue
        for v,w in adj[u]:
            nd = d+w
            if nd < dist[v]:
                dist[v]=nd; heapq.heappush(pq,(nd,v))
    mx = max(range(n), key=lambda i: dist[i] if dist[i]<INF else -1)
    return mx, dist[mx], dist

def multi_min_leaf_pair(n, adj):
    deg = [len(adj[i]) for i in range(n)]
    leaves = [i for i in range(n) if deg[i]==1]
    if len(leaves) < 2: 
        return 0
    
    best_src = [-1]*n
    best_dist = [INF]*n
    pq = []
    for leaf in leaves:
        heapq.heappush(pq, (0, leaf, leaf))
    ans = INF
    while pq:
        d,u,src = heapq.heappop(pq)
        if best_src[u] == -1:
            best_src[u]=src
            best_dist[u]=d

            for v,w in adj[u]:
                if best_src[v] != -1 and best_src[v] != src:
                    ans = min(ans, best_dist[u] + w + best_dist[v])

            for v,w in adj[u]:
                heapq.heappush(pq, (d+w, v, src))

        elif best_src[u] != src:
            ans = min(ans, d + best_dist[u])
    return int(ans)

def main():
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        p,q,w = map(int, input().split())
        adj[p].append((q,w))
        adj[q].append((p,w))

    cn, cadj = compress_tree(n, adj)
    if cn <= 1:
        print(0); print(0); return

    a,_,_ = dijkstra_furthest(0, cn, cadj)
    b,diam,_ = dijkstra_furthest(a, cn, cadj)
    print(int(diam))
    print(multi_min_leaf_pair(cn, cadj))

if __name__ == "__main__":
    main()
