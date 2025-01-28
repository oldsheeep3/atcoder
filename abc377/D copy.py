from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N,M = map(int,input().split())
LR = [list(map(int,input().split())) for _ in range(N)]
LR.sort()
lasti = [0,0]
histM = []
histL = []
xx = []

cmbMin = []
maxa = 0
mina = 200000
for i in LR:
    if i[0] != lasti[0]:
        histM.append(i)
        cmbMin.append(cmb(i[1]-i[0]+1,2)-1+i[1]-i[0])
        if lasti not in histM:
            histL.append(lasti)
        if lasti[1] < i[0] and lasti != [0,0]:
            xx.append([lasti[1],i[0]])
    lasti=i
histL.append([M,M])



print(histM)
print(cmbMin)
print(sum(cmbMin))
print(histL)
print(xx)