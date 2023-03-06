#Mayor que # y menor que #

num1 = int(input("Digite el num1: "))
num2 = int(input("Digite el num2: "))


# if es una codicion verdadera
if num1 > num2:
    print("El numero1 es mayor que el numero2")
    print ("Ejemplo")
    print (num1, ">" ,num2)

#elif en una codicion de que si no es verdadera, preguntara de un porque
elif num2 > num1:
    print("El numero2 es mayor que el numero1")
    print ("Ejemplo")
    print (num2, ">" ,num1)

#else es una codicion falsa
else:
    print("Son iguales")
    print ("Ejemplo")
    print (num2, "=" ,num1)
    