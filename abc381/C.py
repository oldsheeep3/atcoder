import itertools
N = int(input())
S = list(input())
s = [(k, len(list(g))) for k, g in itertools.groupby(S)]
print(s)
ans = {}
ansarr = []
if s[0][0] == "/":
    ansarr.append(("OK",s[0][1]))
elif s[0][0] == "2":
    ansarr.append(("x",s[0][1]))
elif s[0][0] == "1":
    ansarr.append(("?",s[0][1]))
ansarr.append(("?",0))

for i in range(1,len(s)-1):
    if s[i][0] == "/":
        if s[i-1][0] == "1" and s[i+1][0] == "2":
            if s[i-1][1] == s[i+1][1]:
                ansarr[-2] = ("OK",0)
                ansarr[-1] = ("OK",s[i-1][1]+s[i][1]+s[i+1][1])
                ansarr.append(("OK",0))
            elif s[i-1][1] < s[i+1][1]:
                ansarr[-2] = ("OK",0)
                ansarr[-1] = (s[i+1][0],s[i+1][1] - s[i-1][1])
                ansarr.append(("x",0))
            else:
                ansarr[-2] = ("x",0)
                ansarr[-1] = (s[i-1][0],s[i-1][1] - s[i+1][1])
                ansarr.append(("OK",0))
        else:
            if ansarr[-2][0] == "?":
                ansarr[-2] = ("x",0)
                ansarr[-1] = ("OK",s[i][1])
                if s[i+1][0] == "2":
                    ansarr.append(("x",0))
                else:
                    ansarr.append(("?",0))
    elif s[i][0] == "1":
        if ansarr[-2] == "?":
            if s[i-1][0] == "/":
                ansarr[-2] = ("o",s[i-1][1])
            else:
                ansarr[-2] = ("x",0)
        if ansarr[-1] == "?":
            if s[i+1][0] == "2":
                ansarr[-1] = ("x",0)
                ansarr.append(("x",0))
            else:
                ansarr.append(("?",0))
        else:
            ansarr.append(("x",0))
    else:
        if ansarr[-2] == "?":
            if s[i-1] == "/":
                pass
            else:
                ansarr[-2] = ("x",0)
                ansarr[-1] = ("x",0)
        if s[i+1] == "/":
            ansarr.append(("OK",s[i+1][1]))
        else:
            ansarr.append(("?",0))

print(ansarr)
'''
/ 1 2 / x x
/ 1 / / ? ?
2 1 2 ? x x
2 1 / ? ? ?

/ 2 1 ? ? ?
/ 2 / ? ? /
1 2 1 x x ?
1 2 / x x /

1 / 1 x / x
1 / 2 o o o
2 / 1 x / ?
2 / 2 ? / x'''