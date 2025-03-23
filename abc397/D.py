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

from math import sqrt

def factorization(n):
    factors = []
    if n < 1:
        return [-1]
    elif not isinstance(n, int):
        return [-1]
    elif n == 1:
        return [1]

    n1 = n
    for i in range(2, int(sqrt(n))+1):
        if n1 % i == 0:
            while n1 % i == 0:
                n1//=i
                factors.append(i)
                if n1 == 1:
                    return factors
    if n1 != 1:
        factors.append(n1)
        return factors
    elif factors == []:
        return [n]

def y(d):
    D = -3*d*pow(d,4) + 12*N*d
    if D < 0:
        return -1
    return((-3 * pow(d,2) + sqrt(D)) / (6 * d))
N = in1()
ans = -1
maxXY = 1000000

result = factorization(N)
result.append(1)
y(1)
for i in result:
    ys = y(i)
    if ys > 0 and ys.is_integer():
        ys = int(ys)
        print(ys+i,ys)
        break
else:
    print(-1)