N = int(input())
d = []
for n in range(N):
    dd=int(input())
    d.append(dd)
m=1
db = sorted(d)
for n in range(N):
    if n+1 >= N:
        pass
    elif db[n] == db[n+1]:
        pass
    else:
        m=m+1
print(m)