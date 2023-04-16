'''Calcula la Hipotenusa. Para ello, pide al usuario que te de el valor de los catetos. 
Por seacaso, comprueba que los catetos son mayores a 0. 
Hasta que estos datos sean validados no calcular.'''


cat1 = float(input("Ingrese el valor del primer cateto -> "))
cat2 = float(input("Ingrese el valor del segundo cateto -> "))

while cat1 <= 0 or cat2 <= 0:
    print("Los valores ingresado no son validos, ambos catetos deben ser mayores")
    cat1 = float(input("Ingrese el valor del primer cateto -> "))
    cat2 = float(input("Ingrese el valor del segundo cateto -> "))

hipo = (cat1**2 + cat2**2)**0.5
print(f"La hipotenusa del triangulo rectangulo es: {hipo}")

''' Diseñar una calculadora que se enciende y hasta que no tecleamos ‘SAL’ no se apaga.

Esta calculadora funciona de la siguiente manera:

Recogemos los datos A y B
Si operación es 1 calcula la raíz cuadrada de la suma de A y B
Si operación es 2 calcula A / B. Vigilamos que B no sea 0…
Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5 '''

import math

while True:
    print("Bienvenido a su calculadora")
    a = float(input("Ingrese el valor de A -> "))
    b = float(input("Ingrese el valor de B -> "))
    
    while True:
        menu = input('''
                        Menu
                    1 calcula la raíz cuadrada de la suma de A y B
                    2 calcula A / B.
                    3 calculamos la siguiente fórmula: ( A * B ) / 2.5
                    4 salir
                    Que operacion desea realizar -> ''')
        
        if menu == "1":
            res = math.sqrt(a + b)
            print(f"El resultado es {round(res,2)}")
            break
        
        elif menu == '2':
            if b != 0:
                res = a / b
                print(f"El resultado es: {round(res,2)}")
                break
            else:
                print("El divisor no puede ser 0")
        
        elif menu == "3":
            res = (a * b)/ 2.5
            print(f"El resultado es: {round(res,2)}")
            break
        
        elif menu == "salir" or menu == "4":
            print("Gracias por utilizar la calculadora")
            exit()
        
        else:
            print("Opcion invalida, ingrese una de las que se encuentran en el menu")
            
