#capturar 3 numeros y decir cual es mayor y cual es menor, cual es igual o diferente
numero1 = int (input ("digite el numero") )
numero2= int (input ("digite el numero") )
numero3= int (input ("digite el numero") )

if numero1 == numero2 == numero3 :
 
 print ( " los tres numeros son iguales  " ) 

else:
    if numero1 > numero2 and numero1 > numero3:
        print ( "el numero mayor es ", numero1) 
    
    elif numero2 > numero1 and numero2 > numero3 :
              print ("el numero mayor es", numero2)
    else: 
           print("el numero mayor es ",numero3)

           if numero1 < numero2 and numero1 < numero3:
            print(" el numero menor es ", numero1)
           elif numero2 < numero1 and numero2 < numero3: 
            print (" el numero menor es ", numero2)
           else:
            print ( "el numero menor es ", numero3)
            if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
             print ("hay numeros iguales ")
            else:
                print ( "los numeros son diferentes ")
                












