#Nivel principianteEjercicio 6: Juego de adivinanzas

#Crea un programa que "piense" en un número secreto entre 1 y 100.

#Pídele al usuario que adivine el número.

#Dale pistas: "El número es más alto" o "El número es más bajo".

#El juego termina cuando el usuario adivina el número.

#Pista: El módulo random te permite generar un número aleatorio.
#datos de entrada: numero
#Ingreso el numero, despues el programa me dice este numero es mas alto o mayor, hasta llegar al numero correcto hasta el 100
#datos de salida:tres respuesta a) El número es más alto b) El número es más bajoc) adivinaste el numero!

import random



numberRandom = random.randint(1,100)

numero = 1

while numero != numberRandom:
    numb = input("Ingresa un numero del 1 al 100")
    numero=int(numb)

   
        
    if numberRandom > numero:
        print("El numero es mas alto")
        
    elif numberRandom < numero:
        print("el numero es mas bajo")
        
    

print("Adivinaste el numero")

print(numberRandom)


    

    