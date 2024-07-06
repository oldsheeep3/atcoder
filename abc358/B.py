N,A = map(int,input().split())
T = list(map(int,input().split()))
time = 0
for n in range(N):
    if time >= T[n]:
        time = time + A
    else:
        time = T[n] + A
    print(time)