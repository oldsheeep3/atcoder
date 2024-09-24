N = int(input())
H = list(map(int,input().split()))
h = sorted(H)
count = 0
maxs = 0
ans = [0 for _ in range(N)]


MAX = []
def hwc(i):
    if H[i] > H[i+1]:
        MAX.append(H[i])
    if MAX in range(H[i]):
        MAX.remove(H[i])
    return MAX

for i in range(N-1):
    if H[N-i-1] < H[N-i-2]:
        if max(H[N-i-2],maxs) == H[N-i-2]:
            ans[N-i-2] = ans[N-i-1] + 1
        else:
            ans[N-i-2] = ans[N-i-1]
        count = 0
    else:
        ans[N-i-2] = hwc(N-i-1)
print(*ans)