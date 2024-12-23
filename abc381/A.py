import itertools
N = int(input())
S = input()
ss = {k:len(list(g)) for k, g in itertools.groupby(list(S))}
if(S=="/"):
    print("Yes")
else:
    try:
        s = list(S.split("/"))
        s1 = list(s[0])
        s2 = list(s[1])
    except:
        print("No")
    else:
        if(S[0] == "/" or S[-1] == "/"):
            print("No")
        elif(ss["/"] != 1):
            print("No")
        elif(len(s) > 3):
            print("No")
        elif("2" in s1):
            print("No")
        elif("1" in s2):
            print("No")
        elif(len(s1) != len(s2)):
            print("No")
        else:
            print("Yes")
