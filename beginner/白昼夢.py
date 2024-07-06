S = input()
sa = S
while True:
    if sa[-5:]== "dream" or sa[-5:]=="erase":
        sa = sa[:-5]
    elif sa[-6:]=="eraser":
        sa = sa[:-6]
    elif sa[-7:]=="dreamer":
        sa = sa[:-7]
    elif len(sa)==0:
        print("YES")
        break
    else:
        print("NO")
        break