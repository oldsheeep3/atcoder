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

from collections import Counter,defaultdict

N = in1()
A = inl()
ans = 0
cf = Counter(A)
cb = defaultdict(int)
for i in A:
    cf[i] -= 1
    cb[i] += 1
    if cf[i] == 0:
        del cf[i]
    f = len(cf)
    b = len(cb)
    ans = max(ans, f + b)
    if ans >= N:
        break

print(ans)