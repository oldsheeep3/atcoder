A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0
Xd = X

for n in range(A+1):
    if Xd > 0:
        Xd2 = Xd
        for m in range(B+1):
            if Xd2 > 0:
                Xd3 = Xd2
                for o in range(C+1):
                    if Xd3 == 0:
                        count = count+1
                    elif Xd3 < 0:
                        break
                    Xd3 = Xd3 -50                      
            elif Xd2 == 0:
                count=count+1
            else:
                break
            Xd2 = Xd2 - 100
    elif Xd == 0:
        count=count+1
    else:
        break
    Xd = Xd - 500

print(count)