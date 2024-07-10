qname = "./ICPC2023/B1"
fin = open(qname,'r')
fout = open(qname+"-ans","w")
n,m,p,q = map(int,fin.readline().split())
while n > 0:
    ans =""
    x = list(map(int,fin.readline().split()))
    for j in range(m+m+3):
        dp = int(p)
        s = 1
        y = -1
        for i in range(m):
            if i+i+2 == j and dp < n and s == 1:
                ax = int(dp)
                dp += 1
                s = 2
            elif i+i+1 == j and dp > 1 and s == 1:
                dp -= 1
                ax = int(dp)
                s = 2
            if x[i] == dp:
                dp +=1
            elif x[i]+1 == dp:
                dp -=1
        if dp == q:
            y = (j-1)//2
            break
    if dp != q:
        ans = "NG"
    elif y == -1:
        ans = "OK"
    else:
        ans = str(ax) + " " + str(y)
        y = -1

    fout.write(str(ans)+"\n")
    n,m,p,q = map(int,fin.readline().split())
fin.close()
fout.close()
print("comp")