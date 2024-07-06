Sx,Sy = map(int,input().split())
Tx,Ty = map(int,input().split())
if Sx%2 == Sy%2:
    Sx += 1
elif Tx%2 == Ty%2:
    Tx += 1
dx = abs(Sx-Tx)
dy = abs(Sy-Ty)
ddx = max((dx-dy)//2, 0)
print(dy + ddx)