card = list(map(int,input().split()))
ans = {}
for i in card:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1
if (max(ans.values()) + min(ans.values()) == 4) and len(ans) == 2:
    print('Yes')
else:
    print('No')