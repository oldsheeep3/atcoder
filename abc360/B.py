S,T = map(str,input().split())
n = len(S)//len(T)
ans = 1
for i in range(n):
    if S[i:i+len(T)*n:n] == T:
        ans *= 0
        break
    elif S[i:i+(len(T)+1)*n:n+1] == T:
        ans *= 0
        break
if ans == 0 and len(S) != n:
    print("Yes")
else:
    print("No")