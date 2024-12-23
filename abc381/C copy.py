import itertools
N = int(input())
S = list(input())
s = [(k, len(list(g))) for k, g in itertools.groupby(S)]
ans = []
for i in range(1,len(s)-2):
    if s[i-1][0] == "1" and s[i][0] == "/" and s[i+1][0] == "2" and s[i][1] == 1:
        ans.append(2*min(s[i-1][1],s[i+1][1])+1)
    elif s[i][0] == "/":
        ans.append(s[i][1])
if s[0][0] == "/":
    ans.append(s[0][1])
if s[-1][0] == "/":
    ans.append(s[-1][1])
# print(s)
# print(ss)
print(s)
print(ans)

print(max(ans))
