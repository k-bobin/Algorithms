a, b = input().split()
cnt = 1

while b != a and b != '' and int(b) > int(a): 
    if b.endswith('1'):
        b = b[:-1]
        cnt += 1 
    elif int(b) % 2 == 0:
        b = str(int(b) // 2)
        cnt += 1
    else:
        break


if b == a:
    print(cnt)
else:
    print(-1)