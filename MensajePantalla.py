#Escribe un programa que le solicite al usuario su edad y la guarde en una variable.
#que luego solicite la cantidad de articulos comprados en una tienda
#y la guarde en otra variable. finalmente, mostrar en pantalla un valor
#de verdad (true o false) que indique si el usuario es mayor de 
#18 años de edad y ade3mas compro mas de 1 articulo.

edad = int(input("ingresar la edad: "))
articulos = int(input("ingresar el articulo: "))

if edad > 18:
    if articulos > 1:
        print(True)
    else:
        (False)
else:
    print(False)
