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
server = [[i] for i in range(N+1)]
serverInd = [[] for _ in range(N+1)]

def sortBigNum(lst):
    return(min(lst),max(lst))

def sortby(lst,index):
    return sorted(lst, key=lambda x:[index])

AB = [sortBigNum(list(map(int,input().split()))) for _ in range(M)]
AB = sortby(AB,0)
for i,j in AB:
    serverInd[j].append(i)
    server[min(serverInd[j])].append(j)
print(server)
print((len(server)- server.count([]))//2)