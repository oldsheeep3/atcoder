import re
S = input()
ans = 1
if(len(S)%2 == 1):
    print("No")
else:
    s = [S[i:i+2] for i in range(0,len(S),2)]
    if len(s) != len(list(set(s))): 
        print("No")
    else:
        for i in s:
            if(i[0]==i[1]):
                ans *= 1
            else:
                ans *= 0
                break
        if(ans==1):
            print("Yes")
        else:
            print("No")