## 二分探索 ==================================

import bisect

A = range(10) # 配列
val = 5 # 検索する数値
A.sort()
bisect.bisect_left(A,val) # 適切な位置のインデックスを返す (同じのがあるとき一番最初に入れる)
bisect.bisect_right(A,val) # 適切な位置のインデックスを返す (同じのがあるとき一番最後に入れる)
bisect.insort_left(A,val) # 適切な位置にぶち込む (同じのがあるとき一番最初に入れる)
bisect.insort_right(A,val) # 適切な位置にぶち込む (同じのがあるとき一番最後に入れる)

## ダイクストラ =============================

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

## n進数 ==================================
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

# [int,int, ... ] -> {int:[index],int:[index]...}=====================
def intIndex(lst,len=False,dict=True):
    index_dict = {}
    index_len = {}
    for index, value in enumerate(lst):
        if value not in index_dict:
            index_dict[value] = [index]
        else:
            index_dict[value].append(index)
    if len and dict:
        return(index_dict,[len(i) for i in index_dict])
    if len:
        return [len(i) for i in index_dict]
    return index_dict

# n番目のindexでソート ==================
def sortby(lst,index):
    return sorted(lst, key=lambda x:[index])

# lst1 が lst2 の部分集合か否か =========
def listMatch(lst1,lst2):
    return set(lst1).issubset(lst2)

# dfs 辺の重さのリストを返す =============
# graph = {start_node:[(end_node, weight), ...], ...}
def dfs2(graph, node, end_node, visited=set(), weights=[], all_paths=[]):
    visited.add(node)
    if node == end_node:
        all_paths.append(weights.copy())
    else:
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                weights.append(weight)
                dfs(graph, neighbor, end_node, visited, weights, all_paths)
                weights.pop()
    visited.remove(node)
    return all_paths # [[0, 0, 0, ...], ...]

# dfs
# graph = {'A': ['B', 'C'],'B': ['D'],'C': ['D'],'D': []}
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node)  # 現在のノードを出力

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# bfs
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)  # 現在のノードを出力

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# input =================================
def in1(type=int):
    if type == int:
        return int(input())
    return input()
def ins(type=int):
    if type == int:
        return map(int,input().split())
    return map(str,input().split())
def inl(type=int):
    if type==int:
        return list(map(int,input().split()))
    return list(map(str,input().split()))
def inll(n,type=int):
    if type==int:
        return [list(map(int,input().split())) for _ in range(n)]
    return [list(map(str,input().split())) for _ in range(n)]
def yes():
    print('Yes')
def no():
    print('No')
