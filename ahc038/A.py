import numpy as np

N,M,V = map(int,input().split())
s = [list(map(int,input().split())) for _ in range(N)]
t = [list(map(int,input().split())) for _ in range(N)]

# V = 頂点数

def move(pos,dir):
    #U,R,D,L ↑→↓←
    d = {"U":[0,1],"D":[1,0],"L":[0,-1],"R":[-1,0]}
    out = [[i[0] + d[dir][0],i[1] + d[dir][1]] for i in pos if max(i) <= N and min(i) >= 0]
    if len(out) != len(pos):
        out = pos
        dir = "-"
    return [out,dir]

def rotate(pos,dir):
    #R,L 時計,反時計
    d = {"R":[],"L":[]}

    if :
        out = pos
        dir = "."
    return [out,dir]