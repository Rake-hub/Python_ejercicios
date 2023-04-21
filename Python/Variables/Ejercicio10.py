#Ley de Ohm V=RI

def Ohm(a, b):
    return (a*b)

a = int(input('Resistencia (Ω): '))
b = int(input('Amperios (A): '))

print(f'Voltaje total: {Ohm(a, b)} Voltios (V)')