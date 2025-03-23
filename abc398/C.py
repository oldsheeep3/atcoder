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
A = inl()

a = collections.Counter(A)
tmp = -1
for i,j in a.items():
    if j == 1:
        tmp = max(tmp,i)
if tmp == -1:
    print(-1)
else:
    print(A.index(tmp)+1)