c = list(map(str,input().split()))
S = list(input())
S = [c[2] if i != c[1] else i for i in S]
print(*S,sep='')