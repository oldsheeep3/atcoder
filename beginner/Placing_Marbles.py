s= int(input())
print("{}".format(int(float(s/100)+s%10+((s-s%10)%100)/10)))