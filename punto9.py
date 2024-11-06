#ordenar los numeros de mayor a menor

numero1= int(input("digite el numero"))
numero2= int (input("digite el numero"))
numero3= int(input ("digite le numero"))

if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
  print ("Los numeros ordenados de mayor a menor son:", numero1, numero2, numero3)
elif numero2 > numero1 and numero2 > numero3 and numero3 > numero1:
 print ( "los numeros ordenados de mayor a menor son: ", numero2, numero3, numero1)
else: 
  print ("los numeros ordenados de mayor a menor son: ", numero3, numero2, numero1)
  





