nombre = False
while True:
    nombre = input("Su nombre por favor : ")
    if nombre.isdigit():
        print("nombre no valido")
    elif nombre.isalpha():
        print(f"BIENBENIDO¡¡{nombre}!!")
    elif nombre.isalnum():
        print(f"BIENBENIDO¡¡{nombre}!!")








