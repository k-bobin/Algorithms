from itertools import combinations
n,m=map(int,input().split())
password=input().split()
password.sort()
words=list(combinations(password,n))

for answer in words:
	con=0
	vow=0
	for word in answer:
		if word in ['a','e','i','o','u']:
				vow+=1
		else: 
			con+=1
	if vow>=1 and con>=2:
			print(''.join(list(answer)))