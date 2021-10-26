
fib = [0 , 1]

n = int(input('Enter the length of the trail: '))

for i in range(2,n):
    x = fib[i-2] + fib[i-1]
    fib.append(x)


print ('fibonacci : ', fib)
