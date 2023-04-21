#Calcular circunferencia y diametro del circulo a partir del radio

import math 

def dia(r):
    return (r*2)

def cir(r):
    return (dia(r)*math.pi)

r = int(input('Escribir radio (cm): '))

print(f'Diametro: {dia(r)} cm')
print(f'Circunferencia: {cir(r)} cm')
