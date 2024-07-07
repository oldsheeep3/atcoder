import re
S,T = map(str,input().split())
s=[[-1]]
sc = []
for i in range(len(T)):
    s.append([m.start() for m in re.finditer(T[i],S)])
print(s)
for i in range(len(s)-2):
    if s[i+1]:
        ans = 1
        for j in range(len(s[i])):
            for k in range(len(s[i+1])):
                
                    if (s[i+1][k] - s[i][j]) == :
                        ans *= 0
                    else:
                        ans *= 1
        if ans == 1:
            print("No")
            break
    else:
        print("No")
        break
if ans == -0:
    print("Yes")

#for i in s[0]:
#    for j in range(len(sc)-1):
