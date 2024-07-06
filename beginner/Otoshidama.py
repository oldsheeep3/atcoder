import math
N,Y = map(int,input().split())
check = 0
for n in range(int(math.floor(Y/10000))+1):
    if check == 1:
        break
    elif int(math.floor(Y/10000)) > N:
        pass
    else:
        x = n
        Y2 = Y - 10000*x
        for m in range(int(math.floor(Y2/5000))+1):
            if int(math.floor(Y2/5000)) > N - x or Y2 < 0:
                pass
            else:
                y = m
                Y3 = Y2 - 5000*y
                if Y3/1000 == N - x - y:
                    z = N - x - y
                    print("{} {} {}".format(x,y,z))
                    check = 1
                    break
if check == 0:
    print("-1 -1 -1")     