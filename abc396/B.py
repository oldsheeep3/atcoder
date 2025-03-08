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

cards = []
Q = in1()
for _ in range(Q):
    query = inl()
    if query[0] == 1:
        cards.append(query[1])
    else:
        if len(cards) == 0:
            print(0)
        else:
            print(cards[-1])
            cards = cards[:-1]
