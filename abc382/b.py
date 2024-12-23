N,D = map(int,input().split())
S = list(input())
at = S.count('@')
pas = at - D
k = 0
for i,j in zip(S,range(N)):
    if i == "@":
        if k >= pas:
            S[j] = '.'
        k += 1
print(''.join(S))
