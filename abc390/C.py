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

H,W = ins()
S = [list(input()) for _ in range(H)]
blw = W-1
bmw = 0
blh = H -1
bmh = 0
for i,j in zip(S,range(H)):
    if "#" in i:
        blh = min(j,blh)
        bmh = max(j,bmh)
    for k,l in zip(i,range(W)):
        if k == "#":
            blw = min(l,blw)
            bmw = max(l,bmw)
for i in S[blh:bmh+1]:
    # print(i[blw:bmw+1])
    for j in i[blw:bmw+1]:
        if j == ".":
            no()
            break
    else:
        continue
    break
else:
    yes()
