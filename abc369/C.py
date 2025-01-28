from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N = int(input())
A = list(map(int,input().split()))
B = [1 for _ in range(N-1)]
ans = N
if N > 2:
    ab = -1
    for i in range(N-1):
        a = A[i+1]-A[i]
        if ab == a:
            B[i] += B[i-1]
        ab = a
        if B[i] <= B[i-1]:
            ans += cmb(B[i-1]+1,2)
            # print("a"+str(cmb(B[i-1]+1,2)))
    if B[-2] < B[-1]:
        ans += cmb(B[-1]+1,2)
        # print("a"+str(cmb(B[-1]+1,2)))
    if B[-1] != 1:
        ans -= 1
elif N == 2:
    ans += 1
# print(B)
print(ans)
