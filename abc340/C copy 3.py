N=int(input())
print(N*len(bin(N)[3:])+2*(N-pow(2,len(bin(N)[3:]))))