## 二分探索

import bisect

A = range(10) # 配列
val = 5 # 検索する数値
A.sort()
bisect.bisect_left(A,val) # 適切な位置のインデックスを返す (同じのがあるとき一番最初に入れる)
bisect.bisect_right(A,val) # 適切な位置のインデックスを返す (同じのがあるとき一番最後に入れる)
bisect.insort_left(A,val) # 適切な位置にぶち込む (同じのがあるとき一番最初に入れる)
bisect.insort_right(A,val) # 適切な位置にぶち込む (同じのがあるとき一番最後に入れる)

## ダイクストラ

# V: 頂点数
# g[v] = {(w, cost)}:
#     頂点vから遷移可能な頂点(w)とそのコスト(cost)
# r: 始点の頂点

from heapq import heappush, heappop

V, E, start = map(int, input().split()) # V:頂点 E:入力数 start:スタートする点
graph = [[] for _ in range(V+1)]
for _ in range(E):
    s, t, d = map(int, input().split()) # s:始点 t:終点 d:コスト
    graph[s].append((t, d))

INF = pow(10,10) #最大値に合わせて

def dijkstra(graph, goal, start):
    n = len(graph)
    dist = [INF] * n
    que = [(0, start)]
    dist[start] = 0
    while que:
        c, v = heappop(que)
        if dist[v] < c:
            continue
        for t, cost in graph[v]:
            if dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                heappush(que, (dist[t], t))
    return dist

## n進数
# n進数->10進数
def base_10(num_n,n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10

# 10進数->n進数
def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])