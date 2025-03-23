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

N,K = ins()

path = defaultdict(list)
for _ in range(N*K-1):
    v,u = ins()
    path[min(v,u)].append(max(v,u))
for key,value in path:
    print(key)
    print(value)
print(path)