qname = "./ICPC2023/C1"
fin = open(qname,'r')
fout = open(qname+"-ans","w")
n = int(fin.readline())
while n > 0:
    a = [list(map(int,fin.readline().split())) for _ in range(n)]
    b = [[0 for _ in range(n)] for _ in range(n)]
    ml = n//2
    for i in range(n):
        for j in range(n):
            if n%2 == 0:
                b[(ml*i+j)%n][(ml*j+i)%n] = int(a[i][j])
            else:
                b[(ml*i)%n][(ml*j)%n] = int(a[i][j])
    for i in range(n):
        ans = ""
        for j in range(n):
            ans += str(b[i][j]) + " "
        fout.write(ans[:-1] + "\n")
    n = int(fin.readline())
fin.close()
fout.close()
print("comp")