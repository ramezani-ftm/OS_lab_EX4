print('Enter a positive number the sizes (m * n)')
m = int(input('m: '))
n = int(input('n: ')) 
 
def chess(m,n):

    for i in range(m):
        for j in range(n):
            if i%2 == 0:
                if j%2 == 0:
                    print('* ',end='')
                else:
                    print('# ',end='')
            else:
                if j%2 == 0:
                    print('# ',end='')
                else:
                    print('* ',end='')
        print()

chess(m,n)