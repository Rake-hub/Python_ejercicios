#Calcular la hipotenusa

import math

def hip(a, b):
    return (math.sqrt(a**2+b**2))

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Hipotenusa of {a} and {b} is {hip(a, b)}')
