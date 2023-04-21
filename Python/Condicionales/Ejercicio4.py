#Switchcase

a=float(input("Introduce el 1er numero:   "))
b=float(input("Introduce el 2do numero:   "))
op=0

print(" ")

while(True):
    print("¿Qué tipo de operación quieres realizar? (1 a 4)")
    op = int(input("Introduce otro número para salir:       "))

    match op:
        case 1:
            print(a+b)
        case 2:
            print(a*b)
        case 3:
            print(a-b)
        case 4:
            print(a/b)     
        case _:
            print("Saliendo...")
            break

      