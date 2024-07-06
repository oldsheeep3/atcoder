N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
price=[]
Ad = sorted(A)
Bd = sorted(B)
m=0
cc = 1
for n in range(N):
    if m > M-1:
        break
    elif Bd[m] <= Ad[n] and m == M-1:
        price.append(Ad[n])
        ans = 0
        for l in range(M):
            ans = ans + price[l]
        print(ans)
        cc = 0
        break
    elif Bd[m] <= Ad[n]:
        price.append(Ad[n])
        m = m + 1
if cc == 1:
    print("-1")