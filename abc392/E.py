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
server = [[-1] for i in range(N+1)]
serverInd = [[] for _ in range(N+1)]

def sortBigNum(lst):
    return(min(lst),max(lst))

AB = [sortBigNum(list(map(int,input().split()))) for _ in range(M)]
AB.sort(key=lambda x: x[0])

server[0] = []
print(AB)
for i,j in AB:
    serverInd[j].append(i)
    server[min(serverInd[j])].append(j)
    if -1 in server[i]: server[i].remove(-1)
    if -1 in server[j]: server[j].remove(-1)
print(serverInd)
print(server)
serverCheck = [i for i in range(N+1) if server[i] != []]
serverWired = [i for i in serverCheck if server[i] != [-1]]
serverUnWired = [i for i in serverCheck if i not in serverWired]
if server.count([]) == N:
    print(0)
index = 1
for i in serverWired:
    print(serverUnWired[index],i,)
print(serverCheck)
print(serverWired)
print(serverUnWired)