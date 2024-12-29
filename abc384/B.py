N,R = map(int,input().split())
DA = [list(map(int,input().split())) for _ in range(N)]
# print(DA)

def pointup(da,pts):
    if da[0] == 1:
        if 1600 <= pts <= 2799:
            return(pts+da[1])
    else:
        if 1200 <= pts <= 2399:
            return(pts+da[1])
    return pts

ans = R
for i in DA:
    ans = pointup(i,ans)
print(ans)