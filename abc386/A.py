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

card = inl()
ans = {}
for i in card:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1
if (max(ans.values()) + min(ans.values()) == 4) and len(ans) == 2:
    yes()
else:
    no()