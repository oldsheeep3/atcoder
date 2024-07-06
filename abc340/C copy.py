N = int(input())
x = [N]
y = list(x)
pay = 0
stop = False
while max(x) >= 2:
    for n in range(len(x)):
        if x[n] > 1:
            if x[n]%2 == 0:
                y.append(int(x[n]/2))
            else:
                y.append(int(((x[n]-1)/2)))
                y.append(int(((x[n]+1)/2)))
            pay = pay + x[n]
            y.remove(x[n])
    x = list(y)
print(pay)