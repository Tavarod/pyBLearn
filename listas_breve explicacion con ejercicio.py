print('Se crea una variable y despues se le agrega un dato de tipo string con append un texto y distintos numeros')
'''snoopi: list[str | int | float] = []'''
snoopi = ['snoopi es un perrito animado', 55, 0.65, -0.87]
print(snoopi)
snoopi.append(7.65)
snoopi.append(3.1416)
snoopi.append(9.81)
print('\nSe crea una lista y se recorre esta con un, for . ')
batman = [1, 2, 3, 'm', 90.8]
for e in batman:
    print(e)
print('la lista en horizontal')
print(batman)
print('\nSe borran los datos en la Posición numero [2] y [1] a la lista y se remplazan por otros ,')
batman[2] = '♥░*_*░♥'
batman[1] = '○'
print(batman)
print('\nSe inserta el caracter especial ☺ a la Posición (3)\n en el libro se usa '
      '\npunto pero da error al usar una carita feliz por eso la coma ')
batman.insert(3, '☺')
print(batman)
print('\nRemueve el numero de la lista , borra el primero que encuentra si hay mas no los borra ')
batman.remove(1)
print(batman)
print('\nBorra el contenido de la posición [3]')
del (batman[3])
print(batman)
print('Se recorre de nuevo con un ,for, la lista imprime los valores ')
print('\n'
      'se tiene que crear de nuevo nombre,\n por que si se hace con la del primer \n recorrido da una lista erronea')
for a in batman:
    print(a)
print('\n la lista en horizanotal')
print(batman)
print('\n pop ** borra una posicion de la lista en este caso la posicion #3 que corresponde al valor  90.8')
batman.pop(3)
print(batman)
print('sort , sirve para ordenar elementos de una lista \n la lsta batman no se imprime ya que contiene caracteres y'
      ' esto genera error')
spawn = [5, 3, 9, 6, 7, 9, 65, 87, 0, 3, 0.5, -99.3]
'''batman.sort()
    print(batman)'''
print('se imprime una nueva lista que se organizo con ,sort')
spawn.sort()
print(spawn)
print('\n se organiza por que tiene un string, por lo cual antes se borra con un -del- el caracter  ')
del (snoopi[0])
snoopi.sort()
print(snoopi)
print('\n se crea una nueva lista samantha y se une con snoopi y spawn')
samantha = [1982]
samantha = samantha + snoopi + spawn
samantha.sort(reverse=True)
# si se coloca entre la ines 51 y 52 organiza las listas por separado y en la linea 53
# organiza los datos de todas las listas
print(samantha)
