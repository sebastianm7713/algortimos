#ubicar el numero medio entre 3 numeros
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

if (numero1 > numero2 and numero1 < numero3) or (numero1 > numero3 and numero1 < numero2):
              print ("El número medio es:", numero1)

elif (numero2 > numero1 and numero2 < numero3) or (numero2 > numero3 and numero2 < numero1):
 print ("El número medio es:", numero2)
else:
  print ("El número medio es:", numero3)








