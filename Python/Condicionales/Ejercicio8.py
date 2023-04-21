#Comprobar si un año es bisiesto --> 366 días

ano=int(input("Introduce un Año:    "))

def cBisiesto(ano):
    bisiesto=False #Paso 5
    if(ano%4==0): #Paso 1
        if(ano%100==0): #Paso 2
            if(ano%400==0): #Paso 3
                bisiesto=True #Paso 4
        else: bisiesto=True       
    return (bisiesto) #Respuesta

def respuesta(ano):
    r=""
    if (cBisiesto(ano)): r="bisiesto"
    else: r="no bisiesto"
    return r

print(f'El año {ano} es {respuesta(ano)}')