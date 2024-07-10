qname = "./ICPC2023/A1"
fin = open(qname,'r')
fout = open(qname+"-ans","w")
n = int(fin.readline())
while n > 0:
    a = list(map(int,fin.readline().split()))
    ans = 0
    ds = 10000
    for i in range(n):
        if ds > abs(a[i] - 2023):
            ds = abs(a[i] - 2023)
            ans = int(i)+1
        
    fout.write(str(ans)+"\n")
    n = int(fin.readline())
fin.close()
fout.close()
print("comp")
