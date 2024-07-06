N,K = map(int,input().split())
A = list(map(int,input().split()))
n = 0
ans = 0
k = int(K)
while n < N:
    if A[n] <= k:
        k -= A[n]
    else:
        ans += 1
        k = int(K) - A[n]
    n += 1
print(ans+1)