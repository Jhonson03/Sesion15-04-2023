print("Bienvenido a su programa")

vali = True 

while vali == True:
    num = int(input("Ingrese la cantidad de datos a procesar -> "))
    
    if num > 0:
        vali = False
        posi = 0
        nega = 0
        nul = 0
        
        for i in range(num):
            dat = int(input("\nIngrese un numero natural -> "))
            
            if dat > 0: 
                posi += 1
            
            elif dat < 0:
                nega +=1
            
            else:
                nul += 1
        
        print(f"\nLa cantidad de numeros positivos es {posi}")
        print(f"\nLa cantidad de numeros negativos es {nega}")
        print(f"\nLa cantidad de numeros nulos es {nul}")
        
    else:
        print("\nEl numero ingresado no es correcto, intentelo nuevamente")
        
print("Fin del programa")