#Funciones matematicas

"""La sentencia import se usa para importar funciones que han sido
exportadas desde un módulo externo. Nota: Por el momento, 
esta característica sólo está comenzando a ser implementada 
de forma nativa en los navegadores"""
import math

resultado = float(math.sin(math.pi/2))

print(resultado)
print("/////////////////////////////////////////////////////")

decibelio = math.log10(17)
angulo = 1.5
altura = math.sin(angulo)

print (decibelio)
print (altura)

print("/////////////////////////////////////////////////////")
"""La tercera sentencia halla el seno del valor de la variable angulo. 
sin y las otras funciones trigonometricas (cos, tan, etc.) toman 
sus argumentos en radianes. Para convertir de grados a radianes, 
puede dividir por 360 y multiplicar por 2*pi. Por ejemplo, 
para hallar el seno de 45 grados, calcule primero el angulo en 
radianes y luego halle el seno:
"""
grados = 45
angulo = grados * 2 * math.pi / 360
print (math.sin(angulo))

"""La constante pi tambien es parte del modulo math. Si se sabe la 
geometria, puede veriﬁcar el resultado comparandolo con el de la raiz 
cuadrada de 2, dividida entre 2.
"""
#Raiz
resultado1 = math.sqrt(2) / 2
print (resultado1)

print("/////////////////////////////////////////////////////")

x = math.exp(math.log(10))

print(x)

