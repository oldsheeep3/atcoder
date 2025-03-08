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
S = in1()
zero = []
one = []
costs = 0

for i in list(str(S)):
    i = int(i)
    if i == 0:
        costs += 1
    else:
        if len(one) == 0:
            pass
        else:
            zero.append(costs)
        if costs == 0 and len(one) != 0:
            zero[-1]+=1
        else:
            one.append(1)
        costs = 0
ans = 0
while len(zero) > 0  and len(one) > 1:
    if zero[-1]*one[-1] <= zero[0]*one[0]:
        ans += zero[-1]*one[-1]
        one[-2]+=one[-1]
        del zero[-1]
        del one[-1]
    else:
        ans += zero[0]*one[0]
        one[1]+=one[0]
        del zero[0]
        del one[0]
print(ans)