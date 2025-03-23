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

import collections

N = in1()
tree = {i+1:[] for i in  range(N)}
def addTree(v,u):
    if v not in tree[u]:
        tree[u].append(v)
    if u not in tree[v]:
        tree[v].append(u)

tmp = []
for _ in range(N-1):
    u,v = ins()
    addTree(v,u)
# print(tree)
for i in tree.keys():
    if len(tree[i]) == 1:
        tmp.append(i)

tmp.sort()

print(tree)
print(tmp)
if len(tmp)//2%2 == 1:
    print("First")
    print(tmp[0],tmp[1])
    tmp = tmp[2:]
else:
    print("Second")
while True:
    v,u = ins()
    if v == u == -1:
        break
    tmp.remove(v)
    tmp.remove(u)
    print(tmp[0],tmp[1])
    tmp = tmp[2:]
