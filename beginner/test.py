S = list(map(int,input().split()))
ss = 0
for n in range(len(S)):
    ss = ss + S[n]
print(int((ss-max(S)-min(S))/(len(S)-2)))