#Calcular el factorial

def fact(a):
    b=1
    while a>0:
        b*=a
        a-=1
    return (b)

a = int(input('Enter 1st number: '))

print(f'Fact of {a} is {fact(a)}')