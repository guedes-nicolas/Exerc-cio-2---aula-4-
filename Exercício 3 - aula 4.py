print('\n Fatorial \n')

def fatorial(num):
    if num <= 0:
        return(1)
    if num <= 2:
        return(num)
    else:
        return(num * fatorial(num - 1))

num = int(input('Digite um número: '))
fat = fatorial(num)
print(fat)

