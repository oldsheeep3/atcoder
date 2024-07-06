N,M = map(int,input().split())
ans = []
for i in range(N+1):
    ans.append(sum(map(int,str(bin(i&M))[2:])))
print(sum(ans))
