#Determinar si una palabra es un palindromo

word=input("Introduce una nueva palabra:     ")

def separador(word):

    n = 1
    w=[word[i:i+n] for i in range(0, len(word), n)]
    return w

def palindromo (word):
    if(len(separador(word))%2==0):
        
        return True

print (palindromo(word))