for t in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	if n&1:
		print('YES')
	else:
		s=0
		for i in range(1,n,2):
			s+=a[i]-a[i-1]
		print('YES' if s>=0 else 'NO')