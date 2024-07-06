N = int(input())
S = input()
T = input()
s =[]
t =[]
c = 0
for i in range(N):
    s.append(S[i])
    t.append(T[i])
    if S[i] == "W":
        c +=1
    if T[i] == "W":
        c -=1
if c != 0:
    print("-1")
elif S == T[::-1]:
    print(N//2)
else:
    ""