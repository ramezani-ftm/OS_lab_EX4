print('Enter a positive number the sizes (m * n)')
m = int(input('m: '))
n = int(input('n: ')) 

def mul(m,n):
	for i in range(1,m+1):
		for j in range(1,n+1):
			print(i*j, end='\t')
		print()


mul(m,n)