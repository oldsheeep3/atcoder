from heapq import heappush, heappop
def dijkstra(G, s, inf):
    dist = [inf] * len(G)
    dist[s] = 0
    pq = [(0,s)]
    while pq:
        d, v = heappop(pq)
        if d > dist[v]:
            continue
        for u, weight in G[v]:
            nd = d + weight
            if dist[u] > nd:
                dist[u] = nd
                heappush(pq, (nd, u))
    return dist

# N:要素数
# G = [[] for _ in range(N)]
# G[始点] -> (終点,重み)

N,M = map(int,input().split())
UVT = [list(map(int,input().split())) for _ in range(M)]
Q = int(input())
B = [list(map(int,input().split())) for i in range(Q+Q)]
print(B)