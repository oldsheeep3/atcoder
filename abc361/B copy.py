x = list(map(int,input().split()))
xs = list(map(int,input().split()))
ans = 0
for n in range(3):
    if x[n] < xs[n] < x[n+3] or x[n] < xs[n+3] < x[n+3] or (x[n] - xs[n])*(x[n+3] - xs[n+3]) <= 0:
        ans +=1
    else:
        break
if ans == 3:
    print("Yes")
else:
    print("No")