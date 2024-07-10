N,T = map(int,input().split())
S = input()
X = list(map(int,input().split()))
L = []
R = []
for i in range(N):
    if S[i] == "1":
        R.append(X[i])
    else:
        L.append(X[i])
t = T+T+0.2
R.sort()
L.sort(reverse=True)
ans = 0
if R[0] < L[0]:
    for r in R:
        if min(L) - r <= t:
            for l in L:
                if r > l:
                    break
                elif l-r <= t:
                    ans += 1
print(ans)  