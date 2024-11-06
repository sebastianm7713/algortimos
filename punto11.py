#aceptar o rechazar en forma de varilla
longitud = float (input("digite la longitud de la varilla "))
diametro = float ( input ("digite el diametro de la varilla "))
densidad = 3.5
masa = diametro * longitud / densidad

if 7.5 > longitud <= 9 and 0.5 <= diametro <= 1.3 and masa <= 5.8:
    print ("su varilla es aceptable")
else: 
 print ("su varilla no es aceptable")

