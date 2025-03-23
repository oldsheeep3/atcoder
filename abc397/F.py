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

N = in1()
A = inl()
ans = 0
def intIndex(lst,len=False,dict=True):
    index_dict = {}
    index_len = {}
    for index, value in enumerate(lst):
        if value not in index_dict:
            index_dict[value] = [index]
        else:
            index_dict[value].append(index)
    if len and dict:
        return(index_dict,[len(i) for i in index_dict])
    if len:
        return [len(i) for i in index_dict]
    return index_dict

a = intIndex(A)
an = {}
upper = []
mid = []
lower = []
for key, val in a.items():
    val.sort()
    l = len(val)
    if l == 1:
        ans += 1
    else:
        lower.append(val[0])
        upper.append(val[-1])
        if l != 2:
            mid.append(val[1:-1])
    tmp = len(upper)+len(lower)+len(mid)
# print(a)
# print("tmp",tmp)
ll = 0
uu = len(upper)
ml = max(lower)
mu = min(upper)
for i in mid:
    ll = max(bisect.bisect_left(i,ml),ll)
    uu = min(bisect.bisect_left(i,mu),uu)
# print(ll,uu)
ans += tmp - ll - (len(upper) - uu)
# print(upper)
# print(mid)
# print(lower)
print(ans)