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

Q = in1()
hebi = [[0,0]]
head = 0
dec = 0
for i in range(Q):
    b = list(map(int,input().split()))
    if b[0] == 1:
        hebi.append([sum(hebi[-1]),b[1]])
    elif b[0] == 2:
        dec += hebi[head+1][1]
        head += 1
    else:
        print(hebi[head+b[1]][0]-dec)