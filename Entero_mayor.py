print("""
[H]☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻[-][o][x]
♥                                  
♥          ◘BIENVENIDO◘          
♥               \u1696☻\u1696            
♥                                  
☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺
""")

def descending_order(num):
    s_numero = str(num)
    digitos_ordenados = sorted(s_numero, reverse=True)
    highest_num_str = "".join(digitos_ordenados)
    highest_num_int = int(highest_num_str)
    return highest_num_int

"""
la función descending_order paso a paso :

Definición de la función:

python
def descending_order(num):
Aquí defines una función llamada descending_order que acepta un parámetro llamado num.

1 Convertir el número a cadena:

s_numero = str(num)
Esta línea convierte el número recibido como argumento (num) en una cadena de caracteres (s_numero). Esto es necesario 
porque las funciones como sorted() trabajan directamente con cadenas, no con números.

2 Ordenar los dígitos en orden descendente:

digitos_ordenados = sorted(s_numero, reverse=True)
Aquí usas la función sorted() para tomar los caracteres (dígitos) de la cadena s_numero y ordenarlos. 
La opción reverse=True ,que es un argumento, indica que el orden debe ser descendente, de mayor a menor.

sorted(): Esta es una función incorporada de Python. Toma un iterable 
(como una lista, tupla, o en este caso, un string s_numero) 
y devuelve una nueva lista con los elementos del iterable ordenados.

reverse=True: Es un argumento (parámetro opcional) que le pasas a la función sorted(). 
Por defecto, sorted() ordena en orden ascendente (de menor a mayor, o alfabéticamente de A a Z). 
Al poner reverse=True, le indicas a sorted() que quieres el orden descendente (de mayor a menor, o de Z a A).

Por ejemplo, si s_numero = "241", el resultado de sorted(s_numero, reverse=True) será ['4', '2', '1'].

3 Unir los dígitos en una cadena nueva:

highest_num_str = "".join(digitos_ordenados)
Ahora tomas los dígitos ordenados (digitos_ordenados) y los unes en una sola cadena usando "".join(). 
Si los dígitos ordenados son ['4', '2', '1'], el resultado será la cadena "421".

"".join(digitos_ordenados):

.join(): Esto es un método que se llama sobre un objeto string. 
El string sobre el que llamas al método actúa como un "pegamento" o "separador".
"": Este es el string que actúa como separador. En este caso, es un string vacío.
digitos_ordenados: Este es el iterable (la lista que obtuvimos de sorted(), por ejemplo ['5', '4', '4', '2', '1']) 
cuyos elementos se van a unir. Los elementos de este iterable deben ser strings.
Funcionamiento: El método .join() toma cada elemento de la lista digitos_ordenados y los concatena (une) en un solo 
string, poniendo el string separador ("") entre cada elemento. Como el separador es un string vacío, los caracteres se 
pegan directamente uno tras otro.

4 Convertir la cadena nuevamente en número entero:

highest_num_int = int(highest_num_str)
La cadena resultante (highest_num_str) se convierte nuevamente en un número entero para que puedas trabajar con él 
como número y no como texto. Si highest_num_str = "421", el resultado será el número entero 421.

5 Devolver el resultado:

return highest_num_int
Finalmente, la función devuelve el número entero resultante (highest_num_int), que es el número original reorganizado 
con sus dígitos en orden descendente.

Ejemplo:
Si llamas a la función con descending_order(241), el flujo sería así:

s_numero = "241"

digitos_ordenados = ['4', '2', '1']

highest_num_str = "421"

highest_num_int = 421

Resultado: 421
 
"""