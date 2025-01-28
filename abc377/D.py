N,M = map(int,input().split())
ans = 0
mina = 200000
maxa = -1
for _ in range(N):
    a,b = map(int,input().split())
    mina = min(a,mina)
    maxa = max(b,maxa)

for a,b in y:
    ans += a * (M-b)
print(ans)