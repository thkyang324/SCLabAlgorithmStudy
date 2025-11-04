from collections import defaultdict, deque
input=__import__("sys").stdin.readline

N = int(input())
graph = defaultdict(list)
for i in range(N-1):
    p, q, w = map(int, input().split())
    graph[p].append((q, w))
    graph[q].append((p, w))

edges = [node for node in range(N) if len(graph[node]) == 1]

def bfs(start):
    dist = [-1 for _ in range(N)]
    dist[start] = 0
    q = deque([start])

    while q:
        prev = q.popleft()
        for nx, w in graph[prev]:
            if dist[nx] == -1:
                dist[nx] = dist[prev] + w
                q.append(nx)

    max_ = max(range(N), key=lambda x: dist[x])
    return max_, dist[max_], dist

n1, _, _ = bfs(0)
n2, max_, _ = bfs(n1)

min_ = float('inf')

for node in range(N):
    leaf_edges = [w for (nx, w) in graph[node] if len(graph[nx]) == 1]
    if len(leaf_edges) > 1:
        leaf_edges = sorted(leaf_edges)
        min_ = min(min_, leaf_edges[0] + leaf_edges[1])

if min_ == float("inf"):
    _, _, dist = bfs(edges[0])
    min_ = min(dist[e] for e in edges if e != edges[0] and dist[e] > 0)
    
print(max_)
print(min_)