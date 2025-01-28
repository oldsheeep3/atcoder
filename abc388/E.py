import sys
input = sys.stdin.readline
# from operator import itemgetter
# # A.sort(key=itemgetter(1))
# import bisect

# N = int(input())
# A = list(map(int,input().split()))

# ans = 0
# for i in range(N//2):
#     index = bisect.bisect_left(A,A[N-2*i-1]/2)
#     if A[0] <= A[N-2*i-1]/2:
#         del A[N-2*i-1]
#         del A[index-1]
#         ans += 1
#     else:
#         break
# print(ans)

import bisect

N = int(input())
A = list(map(int,input().split()))

ans = 0
Aup = A[:N//2]
Adown = A[(N+1)//2:]
for i in Aup:
    index = bisect.bisect_left(Adown,i*2)
    if Adown[0] >= i*2:
        Adown = Adown[index+1:]
        print(index,'is index')
        ans += 1
    else:
        break
print(ans)