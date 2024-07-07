N = int(input())
A = list(map(int,input().split()))
W = list(map(int,input().split()))
AW = [[] for _ in range(N)]
for i in range(N):
    AW[A[i]-1].append(W[i])
ans = 0
for i in range(N):
    if AW[i]:
        AW[i].remove(max(AW[i]))
        ans += sum(AW[i])

print(ans)