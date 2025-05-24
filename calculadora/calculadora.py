import tkinter as tk
from PIL import Image, ImageTk

# --- Variables Globales ---
expresion = ""  # Almacena la expresión matemática actual como una cadena
visor_texto = None  # Se inicializará como tk.StringVar más adelante
resultado_mostrado = False  # True si el visor muestra el resultado de un cálculo previo

# --- Colores para Botones ---
color_numeros_bg = "#7D2181"      # Púrpura para el fondo de botones numéricos
color_operadores_bg = "#4A2364"   # Violeta profundo para el fondo de botones de operación/otros
color_presionado_bg = "#780606"   # Rojo sangre para cuando se presiona un botón
color_texto_botones = "white"      # Blanco para el texto de los botones
color_texto_presionado = "white"   # Blanco para el texto de los botones cuando están presionados


# --- Funciones Lógicas de la Calculadora ---

def pulsar_tecla(tecla_presionada):
    """
    Añade el carácter de la tecla presionada a la expresión en el visor.
    Si se acaba de mostrar un resultado, inicia una nueva expresión,
    a menos que se presione un operador para continuar el cálculo.
    """
    global expresion, resultado_mostrado

    if resultado_mostrado:
        if tecla_presionada not in ['\u00F7', '\u00D7', '\u2212', '+']:
            expresion = ""
        resultado_mostrado = False

    expresion += str(tecla_presionada)
    visor_texto.set(expresion)

def limpiar_visor():
    """
    Limpia el visor y resetea la expresión y el estado de resultado_mostrado.
    """
    global expresion, resultado_mostrado
    expresion = ""
    visor_texto.set(expresion)
    resultado_mostrado = False

def evaluar_expresion():
    """
    Evalúa la expresión matemática actual en el visor y muestra el resultado.
    Maneja errores comunes como división por cero o sintaxis incorrecta.
    """
    global expresion, resultado_mostrado
    if not expresion:
        return

    try:
        expresion_para_evaluar = expresion.replace('\u00F7', '/') \
                                          .replace('\u00D7', '*') \
                                          .replace('\u2212', '-')

        if not expresion_para_evaluar:
            visor_texto.set("Error")
            expresion = ""
            resultado_mostrado = False
            return

        resultado_calculado = eval(expresion_para_evaluar)

        if isinstance(resultado_calculado, float) and resultado_calculado.is_integer():
            resultado_final_str = str(int(resultado_calculado))
        else:
            resultado_final_str = str(round(resultado_calculado, 10))

        visor_texto.set(resultado_final_str)
        expresion = resultado_final_str
        resultado_mostrado = True

    except ZeroDivisionError:
        visor_texto.set("\U0001F620") # Enojo por dividir por 0
        expresion = ""
        resultado_mostrado = False
    except SyntaxError:
        visor_texto.set("HORROR \U0001F628") # Miedo por error de sintaxis
        expresion = ""
        resultado_mostrado = False
    except Exception as e:
        visor_texto.set("Error")
        print(f"Error inesperado durante la evaluación: {e}")
        expresion = ""
        resultado_mostrado = False

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("Calculadora Rara")

ruta_icono = "C:/Users/Trod/PyCharmMiscProject/Calculadora/calculadora.ico"
try:
    ventana.iconbitmap(ruta_icono)
except tk.TclError:
    print(f"Advertencia: No se pudo cargar el icono desde {ruta_icono}")

ventana.resizable(width=True, height=True)

ruta_imagen_fondo = 'C:/Users/Trod/PyCharmMiscProject/Calculadora/fondo.png'
try:
    imagen_pil = Image.open(ruta_imagen_fondo)
    imagen_pil_redimensionada = imagen_pil.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()), Image.LANCZOS)
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_pil_redimensionada)
    fondo_label = tk.Label(ventana, image=imagen_fondo_tk)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
except FileNotFoundError:
    print(f"Advertencia: No se pudo cargar la imagen de fondo desde {ruta_imagen_fondo}")
except Exception as e:
    print(f"Advertencia: Error al cargar la imagen de fondo: {e}")

# --- Configuración del Visor ---
visor_texto = tk.StringVar()
visor = tk.Entry(
    ventana,
    textvariable=visor_texto,
    font=("Play", 60),
    borderwidth=10, # Usamos borderwidth como especificaste
    justify="right",
    bg="black",
    fg="#00FF00",
    insertbackground="#00FF00",
    relief="sunken",
)
visor.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=20,
    sticky="nsew"
)

# --- Configuración de Filas y Columnas ---
for i in range(6):
    ventana.rowconfigure(i, weight=1)
for i in range(4):
    ventana.columnconfigure(i, weight=1)

# --- Definición y Creación de Botones ---
botones_config = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('\u00F7', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('\u00D7', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('\u2212', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('\u00A9', 4, 2), ('+', 4, 3),
]

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for texto_btn, fila_btn, col_btn in botones_config:
    accion = None
    current_bg_color = ""

    if texto_btn in numeros:
        current_bg_color = color_numeros_bg
    else:
        current_bg_color = color_operadores_bg

    if texto_btn == '\u00A9':
        accion = limpiar_visor
    else:
        accion = lambda char_btn=texto_btn: pulsar_tecla(char_btn)

    boton = tk.Button(
        ventana,
        text=texto_btn,
        font=("Play", 20),
        padx=10,
        pady=10,
        command=accion,
        bg=current_bg_color, # Color de fondo normal
        fg=color_texto_botones, # Color del texto
        activebackground=color_presionado_bg, # Color de fondo cuando está presionado
        activeforeground=color_texto_presionado, # Color del texto cuando está presionado
        relief="raised", # Estilo de relieve para los botones
        bd=3 # Borde del botón
    )
    boton.grid(row=fila_btn, column=col_btn, sticky="nsew", padx=2, pady=2)

# --- Botón de Igual (=) ---
boton_igual = tk.Button(
    ventana,
    text="\U0001F929",
    font=("Play", 30),
    padx=10,
    pady=10,
    command=evaluar_expresion,
    bg=color_operadores_bg, # Es un tipo de operador/acción
    fg=color_texto_botones,
    activebackground=color_presionado_bg,
    activeforeground=color_texto_presionado,
    relief="raised",
    bd=3
)
boton_igual.grid(
    row=5,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=2,
    pady=2
)

# --- Iniciar el Bucle Principal de la Interfaz ---
ventana.mainloop()