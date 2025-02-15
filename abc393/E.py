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
d = {}
def binary_gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if max(a,b)%min(a,b) == 0:
        d[(min(a,b),max(a,b))] = min(a,b)
        return min(a,b)
    a, b = abs(a), abs(b)
    if (min(a,b),max(a,b)) in d.keys():
        return d[(min(a,b),max(a,b))]
    if (a | b) & 1 == 0:  # aとbが偶数の場合
        return binary_gcd(a >> 1, b >> 1) << 1
    if a & 1 == 0:  # aが偶数の場合
        return binary_gcd(a >> 1, b)
    if b & 1 == 0:  # bが偶数の場合
        return binary_gcd(a, b >> 1)
    return binary_gcd(abs(a - b) >> 1, min(a, b))

N,K = ins()
A = inl()
for i in range(N):
    for j in range(N):
        print(binary_gcd(i,j))