import Task1
import Task2
import Task3

def functionMain():

    n = int(input('Enter a positive number: '))
    print(f'For numbers <= {n}\n')
    print(Task1.collatzsequence(n),end='\n\n')
    print(Task2.collatzmax(n),end='\n\n')
    print(Task3.maxValue(n),end='\n\n')


functionMain()
