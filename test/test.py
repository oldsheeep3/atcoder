import numpy as np
dir = "L"

d = {"U":[0,1],"D":[1,0],"L":[0,-1],"R":[-1,0]}
N = 70
pos = [[1,1],[60,60],[1,100],[0,-100]]
out = [[i[0] + d[dir][0],i[1] + d[dir][1]] for i in pos if max(i) <= N and min(i) >= 0]

print(out)