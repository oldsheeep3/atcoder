N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = A[-K:] + A[:-K]
print(*ans)