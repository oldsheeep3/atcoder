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
import bisect

S = list(input())
def ans(lst):
    ls = ""
    for i in lst:
        ls += i
    print(ls)
N = len(S)
s = S[::-1]
if N == 1:
    print(S)
else:
    for i in range(N):
        tmp = S + s[N-i:]
        if tmp[:-(N+i-1)//2] == tmp[(N+i)//2:][::-1]:
            ans(tmp)
            break