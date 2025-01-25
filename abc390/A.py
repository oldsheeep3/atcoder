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

A = inl()
check = []
for i in range(4):
    check.append(A[i+1] - A[i])
# print(check)

if set([2,-1,2]).issubset(check) and sum(check) == 4:
    yes()
elif sum(check) == 3:
    if [-1,2] == check[:2]:
        yes()
    elif [2,-1] == check [-2:]:
        yes()
    else:
        no()
else:
    no()