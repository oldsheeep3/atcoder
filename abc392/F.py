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
N = in1()
P = inl()
ans = [0 for i in range(N)]
sett = [0 for i in range(N+1)]
for i in range(N):
    j = N-i-1
    ans[P[i]-1+sum(sett[:i+1])] = j+1
    sett[P[i]] += 1
    print(sett)
print(*ans)