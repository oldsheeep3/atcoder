N,X,Y = map(int,input().split())
if Y%X == 0:
    print(N//X)
else:
    print(N//X + N//Y - N//(X*Y))