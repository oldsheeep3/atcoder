S = [list(input()) for _ in range(8)]
x = ["o" for i in range(8)]
y = ["o" for i in range(8)]
for i in range(8):
    for j in range(8):
        if S[i][j] == "#":
            x[i] = "x"
            y[j] = "x"
print(x.count("o")*y.count("o"))