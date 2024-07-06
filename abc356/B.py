N,M = map(int,input().split())
A = list(map(int,input().split()))
X = []
for n in range(N):
    X.append(list(map(int,input().split())))
ans = 1
for m in range(M):
    nn = 0
    for n in range(N):
        nn = nn + X[n][m]
    if nn >= A[m]:
        ans = ans*1
    else:
        ans = ans*0
        break
if ans == 0:
    print("No")
else:
    print("Yes")