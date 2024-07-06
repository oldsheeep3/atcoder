N,K = map(int,input().split())
S = input()
s = str(S)
sc = S.count('?')
for j in range(sc):    
    ans = 1
    for i in range(N-K+1):
        s1 = s[i:i+K]
        s2 = s1[::-1]
        print(s1)
        print(s2)
        if s1 != s2:
            ans *= 1
        else:
            ans *= 0
print(ans)