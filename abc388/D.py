N = int(input())
A = list(map(int,input().split()))
Ad = [A[i]+2*i-N+1 for i in range(N)]
ans = []
down = {0:0}
j = 0
for i in range(N):
    ans.append(max(0,A[i]+2*i-N+1))
    if A[i]+2*i-N+1 < 0:
        key = A[i]+2*i-N+1
        if key in down:
            down[key] -= 1
        else:
            down[key] = -1
down = dict(sorted(down.items()))
keys_list = list(down.keys())
dd = 0
for i in range(len(keys_list)-1):
    dd += down[keys_list[i]]
    for j in range(keys_list[i],keys_list[i+1]):
        ans[j] = max(0,ans[j]+dd)
print(*ans)