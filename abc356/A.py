N,L,R = map(int,input().split())

ans = []
ans2 = []
ans3 = ""
m = 0
for n in range(N):
    ans.append(n+1)
for n in range(R-L+1):
    ans2.append(R-n)
for n in range(N):
    if L <= n+1 <= R:
        ans3 = ans3 + " " + str(ans2[m])
        m += 1
    else:
        ans3 = ans3 + " " + str(ans[n])
print(ans3[1:])