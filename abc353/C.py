import itertools
N = int(input())
A = list(map(int,input().split()))
x = 0
for n in itertools.combinations(A, 2):
    x += int(str(sum(list(n)))[-8:])
print(x)