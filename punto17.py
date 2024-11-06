#calcular si el numero es divisble con otro
numero1 = int (input ("digite su numero "))
numero2 = int(input (" digite su numero "))
numero3 = int (input ("digite su numero "))

if numero1 != 0 and numero2 % numero1 == 0:
  print ( "el", numero2 , "es divisible por ", numero1)
elif numero1 != 0 and numero3 % numero1 == 0 :
    print ("el", numero3 , " es divisble por", numero1) 
elif numero2 != 0 and numero1 % numero2 == 0:
        print ("el", numero1, " es divisible por ", numero2)
elif numero2 != 0 and numero3 % numero2 == 0:
   print( "el", numero3, " es divisble por ", numero2)
elif numero3 != 0 and numero1 % numero3 == 0:
  print("el", numero1, "es divisible por", numero3)
elif numero3 != 0 and numero2 % numero3 == 0:
   print("el", numero2, "es divisble por", numero3)
else:
        print ( "ningun numero es divisble entre otro ")
        







