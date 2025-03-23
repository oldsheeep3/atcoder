def in1(type=int):
    if type == int:
        return int(input())
    return input()
def ins(type=int):
    if type == int:
        return map(int,input().split())
    return map(str,input().split())
def inl(type=int):
    if type==int:
        return list(map(int,input().split()))
    return list(map(str,input().split()))
def inll(n,type=int):
    if type==int:
        return [list(map(int,input().split())) for _ in range(n)]
    return [list(map(str,input().split())) for _ in range(n)]
def yes():
    print('Yes')
def no():
    print('No')

from collections import defaultdict
N,R,C = map(int,input().split())
S = input()

smoke = defaultdict(set)
def move(key,now):
    if key == "N":
        return((now[0]-1,now[1]))
    elif key == "E":
        return((now[0],now[1]+1))
    elif key == "W":
        return((now[0],now[1]-1))
    elif key == "S":
        return((now[0]+1,now[1]))
ans = ""
origin = (0,0)
smoke[origin[0]].add(origin[1])
for i in S:
    origin = move(i,origin)
    smoke[-1*origin[0]].add(-1*origin[1])
    if  C-origin[1] in smoke[R-origin[0]]:
        ans += "1"
    else:
        ans += "0"
print(ans)
