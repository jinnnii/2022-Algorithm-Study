s = list(input())
count = 1
result = len(s)
for i in range(1, len(s)):
    short = ''
    for j in range((len(s)//i)-1):
        now = s[j*i:(j*i)+i]
        next = s[(j+1)*i:((j+1)*i)+i]
        if now == next:
            count += 1
        else:
            short += ''.join(now)+(str(count))
            count = 1
    else:
        short += s[i*(len(s)//2):]
        print(i, short)
        rerult = min(result, len(short))
print(result)
