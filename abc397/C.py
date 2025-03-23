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

from collections import Counter
N = in1()
A = inl()
ans = 0
F = A
B = []
cf = Counter(F)  # Fの要素の出現回数をカウント
cb = Counter()    # Bの要素の出現回数をカウント
ans = 0

for i in range(N-1):
    if not F:
        break
    fb = F.pop()
    B.append(fb)
    cf[fb] -= 1
    if cf[fb] == 0:
        del cf[fb]
    cb[fb] += 1
    f = len(cf)
    b = len(cb)
    ans = max(ans, f + b)
    if ans >= N:
        break

print(ans)