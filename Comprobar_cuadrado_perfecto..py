print("""
[H]☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻[-][o][x]
♥                                  
♥          ◘BIENVENIDO◘          
♥               \u221A☻            
♥                                  
☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺
""")

import math

def find_next_square(sq):
    raiz = math.sqrt(sq)
    if raiz.is_integer():
        siguiente_raiz = int(raiz) + 1
        return siguiente_raiz **2
    else:
        return -1


'''
Analisis Python paso a paso:

1 import math

Propósito: Esta línea importa el módulo math de Python.
¿Por qué? El módulo math contiene varias funciones matemáticas útiles. En este código específico, se 
necesita para usar la función math.sqrt(), que calcula la raíz cuadrada de un número.

2 def find_next_square(sq):

Propósito: Define una función llamada find_next_square.
¿Qué hace? Esta función está diseñada para tomar un argumento (un número) que se llamará sq dentro de la función. 
El objetivo de la función es encontrar el siguiente número que sea un cuadrado perfecto después del número sq, pero solo 
si sq es un cuadrado perfecto en sí mismo.

3 raiz = math.sqrt(sq)

Propósito: Calcula la raíz cuadrada del número de entrada sq.
¿Cómo funciona? Llama a la función sqrt() del módulo math pasándole el valor de sq.
Almacenamiento: El resultado de la raíz cuadrada (que podría ser un número entero o con decimales, 
por ejemplo, sqrt(9) es 3.0, sqrt(10) es 3.16...) se guarda en una variable llamada raiz.

4 if raiz.is_integer():

Propósito: Comprueba si el valor almacenado en la variable raiz representa un número entero.
¿Cómo funciona? Los resultados de math.sqrt() son siempre números de punto flotante (floats). 
El método .is_integer() para los floats devuelve True si el número no tiene parte decimal (como 3.0, 12.0) y 
False si tiene parte decimal (como 3.16..., 5.5).
¿Por qué esta comprobación? La función solo debe encontrar el "siguiente cuadrado" si el número de entrada sq era un 
cuadrado perfecto. Si sq es un cuadrado perfecto, su raíz cuadrada (raiz) será un número entero 
(representado como un float sin decimales, ej: 12.0). Si sq no es un cuadrado perfecto, 
su raíz cuadrada tendrá decimales.

5 siguiente_raiz = int(raiz) + 1

Propósito: Si la condición anterior (if raiz.is_integer()) fue True (es decir, sq era un cuadrado perfecto), 
esta línea calcula cuál sería la raíz cuadrada del siguiente cuadrado perfecto.
¿Cómo funciona?
int(raiz): Convierte el valor de raiz (que sabemos que es un entero como 12.0) a un tipo de dato entero (12).
+ 1: Le suma 1 a esa raíz entera (si raiz era 12, ahora siguiente_raiz será 13).

6 return siguiente_raiz ** 2

Propósito: Calcula y devuelve el siguiente cuadrado perfecto.
¿Cómo funciona? Toma el valor de siguiente_raiz (que es la raíz del siguiente cuadrado, por ejemplo 13) y lo eleva 
al cuadrado usando el operador ** 2 ( 13 ** 2 es 169).
return: La palabra clave return finaliza la ejecución de la función y envía este valor calculado 
(el siguiente cuadrado perfecto) como resultado de llamar a la función.

7 else:

Propósito: Define qué hacer si la condición if raiz.is_integer(): fue False.
¿Cuándo ocurre? Esto pasa si el número original sq no era un cuadrado perfecto 
(porque su raíz cuadrada raiz tenía decimales).

8 return -1

Propósito: Si sq no era un cuadrado perfecto, la función devuelve el valor -1.
¿Por qué -1? Es una convención común usar -1 (o a veces None) para indicar que la función no pudo realizar la operación 
solicitada según sus propias reglas (en este caso, la regla era que la entrada debía ser un cuadrado perfecto para 
encontrar el siguiente).

'''