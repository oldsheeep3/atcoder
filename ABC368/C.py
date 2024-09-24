N = int(input())
H = list(map(int,input().split()))


ans = 0
t = 0
for i in range(N):
    ans += (H[i]//5)*3

    h = H[i]%5
    if h <= 1:
        t += h
    elif t%3 == 2:
        if h == 4:
            t += 2
        else:
            t += 1
    elif t%3 == 0:
        if h == 2:
            t += 2
        else:
            t += 3
    elif t%3 == 1:
        t += 2

print(t+ans)