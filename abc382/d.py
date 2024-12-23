N,M = map(int,input().split())
ans = [1 + 10*i for i in range(N)]
a = []
def tenUp(ans,deg):
    if deg < 0:
        while ans[deg]%10 < M%10:
            tenUp(ans,deg+1)
            a.append(ans.copy())
            ans[deg] += 1
            for i in range(deg,-1):
                ans[i+1] = ans[i] + 10
tenUp(ans,-N)
print(len(a) + 1)
for i in a:
    print(*i)
print(*[M%10 + 10*i for i in range(N)])