fname = "./ICPC2023/B1"
ans = open(fname+"-ans","r")
can = open(fname+".ans","r")
c = 1
k = 0
for i,j in zip(ans.read().splitlines(),can.read().splitlines()):
    k+=1
    if i == j:
        c *= 1
    else:
        c *= 0
        print("line"+str(k)+": ("+str(i)+")-("+str(j)+")")
if c == 1:
    print("True")
else:
    print("False")