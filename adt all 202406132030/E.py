N = int(input())
H = list(map(int,input().split()))
h = [H[0]+1]
for i in range(N-1):
    if H[i] > H[i+1]:
        water = h[i] + H[i+1]
    else:
        water = H[i+1]*(i+2)+1
    h.append(water)
print(h)