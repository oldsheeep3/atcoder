x = list(map(int,input().split()))
xs = list(map(int,input().split()))
ans = 0
for n in range(3):
    if min(x[n],x[n+3]) < xs[n] < max(x[n],x[n+3]) or min(x[n],x[n+3]) < xs[n+3] < max(x[n],x[n+3]) or (min(x[n],x[n+3]) - min(xs[n],xs[n+3]))*(max(x[n],x[n+3])-max(xs[n],xs[n+3])) < 0:
        ans +=1
#if x == xs:
#    ans = 3 #これいらなかった...
if ans == 3:
    print("Yes")
else:
    print("No")