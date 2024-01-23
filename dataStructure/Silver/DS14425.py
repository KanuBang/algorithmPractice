n,m = map(int,input().split())

wordSet,cnt = [],0

for i in range(n+m):
    word = input().rstrip()

    if  0<= i and i < n:
        wordSet.append(word)
        continue
    
    cnt += 1 if word in wordSet else 0

print(cnt)

