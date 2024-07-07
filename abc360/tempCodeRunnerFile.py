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
L.sort()
ans = 0
for r in R:
    if min(L) - r > t or max(L) < r:
        pass
    else:
        for l in L:
            if 0 <= l-r <= t:
                ans += 1
            elif l < r:
                break
print(ans)