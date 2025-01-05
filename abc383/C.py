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

def manhatan(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


s = []
h = []
ok = {}
H,W,D = ins()
for i in range(H):
    ss = list(input())
    for j in range(W):
        if ss[j] == 'H':
            h.append((i,j))
    s.append(ss)

def up(now):
    if now[0] > 0:
        return(now if s[now[0]-1][now[1]] == '#' else (now[0]-1,now[1]))
    return now
def down(now):
    if now[0] < H-1:
        return(now if s[now[0]+1][now[1]] == '#' else (now[0]+1,now[1]))
    return now
def right(now):
    if now[1] < W-1:
        return(now if s[now[0]][now[1]+1] == '#' else (now[0],now[1]+1))
    return now
def left(now):
    if now[1] > 0:
        return(now if s[now[0]][now[1]-1] == '#' else (now[0],now[1]-1))
    return now
def kashitu(now,at,ans=0):
    if at > 0:
        for j in [up(now),down(now),left(now),right(now)]:
            if s[j[0]][j[1]] != '*':
                s[j[0]][j[1]] = '*'
                ans = kashitu(j,at-1,ans+1)
    return(ans)
rt = 0
for i in h:
    rt += kashitu(i,D)
for i in s:
    print(i)
print(rt)