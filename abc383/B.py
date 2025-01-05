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

H,W,D = ins()
ans = 2
ss = []
for i in range(H):
    s = list(input())
    for j,k in zip(s,range(W)):
        if j == '.':
            ss.append((i,k))

for i in range(len(ss)-1):
    for j in range(i+1,len(ss)):
        anss = 0
        for k in range(len(ss)):
            # print(ss[i],ss[j],ss[k])
            if manhatan(ss[i],ss[k]) <= D:
                anss += 1
            elif manhatan(ss[j],ss[k]) <= D:
                anss += 1
            # print(anss)
        ans = max(anss,ans)
print(ans)


