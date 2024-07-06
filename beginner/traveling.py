N = int(input())
t = [0]
x = [0]
y = [0]
for n in range(N):
    tt,xx,yy=map(int,input().split())
    t.append(tt)
    x.append(xx)
    y.append(yy)

check = 0

for n in range(N):
    dt = t[n+1]-t[n]
    dx = abs(x[n+1]-x[n])
    dy = abs(y[n+1]-y[n])
    if dx + dy - dt <= 0 and (dx + dy - dt)%2 == 0:
        pass
    else:
        print("No")
        check = 1
        break

if check == 0:
    print("Yes")