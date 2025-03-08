def in1(type=int):
    if type == int:
        return int(input())
    return input()

def ins(type=int):
    if type == int:
        return map(int, input().split())
    return map(str, input().split())

def inl(type=int):
    if type == int:
        return list(map(int, input().split()))
    return list(map(str, input().split()))

N, M = ins()
graph = {i: [] for i in range(1,N+1)}
for _ in range(M):
    u,v,w = ins()
    if v != 1:
        graph[u].append((v,w)) 
    if u != 1:
        graph[v].append((u,w))

# DFSで全てのパスを探す
# graph = {start_node:[(end_node, weight), ...], ...}
def dfs(graph, node, end_node, visited=set(), path_weights=[], all_paths=[]):
    visited.add(node)
    if node == end_node:
        all_paths.append(path_weights.copy())
    else:
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                path_weights.append(weight)
                dfs(graph, neighbor, end_node, visited, path_weights, all_paths)
                path_weights.pop()
    visited.remove(node)
    return all_paths

all_paths = dfs(graph, 1, N)

ans = pow(2,60)+1
for path in all_paths:
    anss= 0
    for i in path:
        anss ^= i
    ans = min(anss,ans)
print(ans)