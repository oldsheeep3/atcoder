
N,D = map(int,input().split())
S = input()
at = min(S.count('@'),D)
dot = S.count('.')
ans = at + dot
print(ans)