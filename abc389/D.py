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
def intt(num):
    return(int(num) if type(num) != int else num)
R = in1()
ans = -R
for i in range(R):
    ans += int(pow(pow(R,2)-pow(i+0.5,2),0.5)+0.5)
print(ans*4+1)