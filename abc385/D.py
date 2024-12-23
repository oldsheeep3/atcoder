import bisect


N,M,X,Y = map(int,input().split())
XY = {}
for _ in range(N):
    a,b = map(int,input())
    bisect.insort(XY[a],b)
DC = [tuple(map(lambda x: x if x.isalpha() else int(x), input().split())) for _ in range(M)]
ans = [X,Y,0]

A = range(10) # 配列
val = 5 # 検索する数値
A.sort()
bisect.bisect_left(A,val)
bisect.bisect_right(A,val)


def move(now,dir):
    if dir[0] == "U":
        first = bisect.bisect_left(XY[now[1]],now[0])
        now[0] -= dir[1]
        second = bisect.bisect_left(XY[now[1]],now[0])
        XY[now[1]] = XY[now[1]][:min(first,second)] + XY[now[1]][max(first,second):]
        ans[2] += abs(first - second)
    if dir[0] == "D":
        first = bisect.bisect_left(XY[now[1]],now[0])
        now[0] += dir[1]
        second = bisect.bisect_left(XY[now[1]],now[0])
        XY[now[1]] = XY[now[1]][:min(first,second)] + XY[now[1]][max(first,second):]
        ans[2] += abs(first - second)
    if dir[0] == "L":
        first = bisect.bisect_left(XY[now[0]],now[1])
        now[1] -= dir[1]
        second = bisect.bisect_left(XY[now[0]],now[1])
        XY[now[1]] = XY[now[0]][:min(first,second)] + XY[now[1]][max(first,second):]
        ans[2] += abs(first - second)
    if dir[0] == "R":
        first = bisect.bisect_left(XY[now[0]],now[1])
        now[1] += dir[1]
        second = bisect.bisect_left(XY[now[0]],now[1])
        XY[now[1]] = XY[now[0]][:min(first,second)] + XY[now[1]][max(first,second):]
        ans[2] += abs(first - second)
    return now

for i in DC:
    ans = move(ans,i)

print(*ans)