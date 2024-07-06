N = int(input())
A = list(map(int,input().split()))
ans = 0
for n in range(2*N-2):
    if A[n] == A[n+2]:
        ans += 1
print(ans)