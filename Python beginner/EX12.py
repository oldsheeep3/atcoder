N = int(input())
T = list(map(int,input().split()))
for n,t in enumerate(T):
    if t == min(T):
        print(n+1)
        break