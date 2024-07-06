N = int(input())
A = list(map(int,input().split()))
ans = 0
for i,a in enumerate(N):
    for j in range(N-i-1):
        ans = ans + (max(a,A[j+i+1]) // min(a,A[j+i+1]))

print(ans)