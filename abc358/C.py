N,M = map(int,input().split())
S=[]
S1=[]
S2=[]
count = 0
for n in range(N):
    Marray = []
    T = input()
    for m in range(len(T)):
        Marray.append(T[m])
    S.append(Marray)

for n in range(N):
    for m in range(M):
        if S[n][m]=="o":
            S[n][m]=1
        else:
            S[n][m]=0
for m in range(M):
    Sn = 0
    for n in range(N):
        Sn = Sn + S[n][m]
        if Sn == 1:
            S1.append([n,m])
            count = count +1
for n in range(len(S1)):
    for m in range(M):
        if S[S1[n][0]][m] == 1 and m != S1[n][1]:
            S1.append([S1[n][0],m])
print(S1)