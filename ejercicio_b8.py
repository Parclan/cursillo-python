"""Ahora que ya sabemos convertir entre tipos, tenemos otra forma de enfrentarnos a la division de enteros. 
Volviendo al ejemplo del capitulo anterior, suponga que 
queremos calcular que fraccion de una hora habia transcurrido. 
La expresion mas obvia, minuto / 60, realiza una division de enteros, 
por lo que el resultado es siempre 0, incluso 59 minutos despues de la hora.

Una alternativa es convetir minuto a tipo ﬂoat (coma ﬂotante) y luego efectuar 
una division de coma ﬂotante:
minuto = 59 
float(minuto) / 60.0 
0.983333333333"""

#Ejercicios

import math
#Aqui puedo utilizar int y float las 2 nos arrojaria el mismo valor
minutos = 59
#int
print (int(minutos)/60)

#Float
print (float(minutos)/60)

print("/////////////////////////////////////////////////////")
print("Actividades")

Resultado = float(math.pi/2)
print(Resultado)

print("/////////////////////////////////////////////////////")

