for i in range(1, 20) : 
    for j in range(1, 20, 2) :
        print(f'{i} * {j} = {i*j}', end=' ')
        if j < 19 :
            print('/', end=' ')
            print(f'{i} * {j+1} = {i*(j+1)}', end='')
        print()