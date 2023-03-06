#Limpiar el termial en visual estudio
import os

if os.name == "nts" :
    os.system ("clear")

else:
    os.system ("cls")

#Este son las varibles para digitar nuestros numeros 
num1 = int(input("Digite el num1: "))
num2 = int(input("Digite el num2: "))

#Este es el print para monstrar el resultado

print("///////////////////////////////////////////")

#Suma
print("Suma")
print(num1 + num2)

print("///////////////////////////////////////////")

#Resta
print("Resta")
print(num1 - num2)

