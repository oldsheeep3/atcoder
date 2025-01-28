N,D = map(int,input().split())
TL = [list(map(int,input().split())) for _ in range(N)]
for i in range(1,D+1):
    print(max([j[0] * (j[1]+i) for j in TL]))