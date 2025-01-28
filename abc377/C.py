N,M = map(int,input().split())
y = [tuple(map(int,input().split())) for _ in range(M)]
x = set()
ans = 0

def notOK(x,y):
    return [(x-1,y-1),(x+1,y),(x,y+1),(x-2,y+1),(x-3,y),(x-3,y-2),(x-2,y-3),(x,y-3),(x+1,y-2)]
def inOut(x,y):
    return 0 <= x < N and 0 <= y < N

for a, b in y:
    for c, d in notOK(a, b):
        if inOut(c, d) and (c, d) not in x:
            x.add((c, d))
            ans += 1

print(pow(N,2) - ans)