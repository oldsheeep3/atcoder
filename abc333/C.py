N = int(input())
X = ["1","1","1"]
n = 1
a = 0
while n < N:
    a = 0
    X[0]=X[0]+"1"
    X[1]="1"
    X[2]="1"
    n+=1
    b = int(len(X[0]))
    while len(X[1]) < b and n < N:
        X[1]=X[1]+"1"
        X[2]="1"
        n+=1
        c = int(len(X[1]))
        while len(X[2]) < c and n < N:
            X[2]=X[2]+"1"
            n+=1
print(int(X[0])+int(X[1])+int(X[2]))