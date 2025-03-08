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

N,M = ins()
B = sorted(inl(),reverse=True)
W = sorted(inl(),reverse=True)
ans = 0
tmp = -1

for i in range(min(N,M)):
    if B[i] > 0 and W[i] <= 0:
        tmp = i
        break
    elif B[i] + W[i] >= 0:
        ans += B[i] + W[i]
    else:
        break
else:
    tmp = min(N,M)
if tmp >= 0:
    pp = [i for i in B[tmp:] if i > 0]
    ans += sum(pp)
print(ans)
