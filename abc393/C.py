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
from collections import defaultdict
N,M = ins()

ans = 0
tree = defaultdict(int)
for _ in range(M):
    v,u = ins()
    if v == u:
        ans += 1
    else:
        tree[(min(u,v),max(u,v))] += 1
for count in tree.values():
    if count > 1:
        ans += count - 1
print(ans)
