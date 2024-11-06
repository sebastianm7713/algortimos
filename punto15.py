#evalue la formula cuadratica o general
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))
discriminante = b**2 - 4*a*c

if a == 0:
    print("El valor de 'a' no puede ser 0, ya que no sería una ecuación cuadrática.")

elif discriminante > 0:
     print("La ecuación tiene dos soluciones reales: x1 = {x1}, x2 = {x2}")

elif discriminante == 0:
 print("La ecuación tiene una solución real doble: x = {x}")
else:
    print("La ecuación tiene soluciones complejas: x1 = {parte_real} + {parte_imaginaria}i, x2 = {parte_real} - {parte_imaginaria}i")