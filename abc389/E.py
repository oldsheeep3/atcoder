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
P = inl()
P.sort()

def price(k,p):
    return(pow(k,2)*p)

def priecup(i,k): # i = なんこめ k = 個数（元） 
    return(2*i*k + i*i)

ans = 0
for i in range(N):
    if M < P[i]:
        break
    plus = int(pow(M/P[i],0.5))
    if plus > P[i+1]:
        plus = int(pow(M/P[i+1],0.5))
    ans += plus
    M -= price(plus,P[i])
print(ans)