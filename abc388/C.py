import bisect

N = int(input())
A = list(map(int,input().split()))
ans = 0
for i in A[:-1]:
    ans += N - bisect.bisect_left(A,i*2)
print(ans)