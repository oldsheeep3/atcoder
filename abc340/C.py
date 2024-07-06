N = int(input())
x = [N]
y = list(x)
pay = 0
stop = False
while stop == False:
    for n in range(len(x)):
        if max(x) <= 1:
            print(pay)
            stop = True
            break
        else:
            if x[n] > 1:
                if x[n]%2 == 0:
                    y.append(int(x[n]/2))
                    y.append(int(x[n]/2))
                else:
                    y.append(int(((x[n]-1)/2)))
                    y.append(int(((x[n]+1)/2)))
                pay = pay + x[n]
                y.remove(x[n])
            else:
                y.remove(x[n])
    x = list(y)