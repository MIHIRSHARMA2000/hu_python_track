row1 = int(input('Enter number of rows required: '))

for i in range(row1):
        for j in range(row1 - i):
            print(' ', end='')
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == row1 - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
