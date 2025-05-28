import tkinter as tk
from tkinter import font as tkFont # Para definir estilos de fuente más fácilmente
from PIL import Image, ImageTk
from cal_ces import calcular_cesantias_valor
from dias import verificar_dia_entero
from salario import obtener_smlv_predeterminado
from sub_trans import calcular_monto_subsidio

# Ventana Principal
ventana = tk.Tk()
ventana.geometry("700x550") # Ajustado el tamaño para el nuevo contenido
ventana.title("Calculadora Cesantías")

# Icono Aplicación
ruta_icono = "C:/Users/Trod/PyCharmMiscProject/calculadora_cesantias/calculadora_cesa.ico"
try:
    ventana.iconbitmap(ruta_icono)
except tk.TclError:
    print(f"Advertencia: No se pudo cargar el icono desde {ruta_icono}")

ventana.resizable(width=True, height=True)

# Fondo Aplicación
ruta_imagen_fondo = 'C:/Users/Trod/PyCharmMiscProject/calculadora_cesantias/fondo.png'
try:
    imagen_pil = Image.open(ruta_imagen_fondo)
    imagen_pil_redimensionada = imagen_pil.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()), Image.LANCZOS)
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_pil_redimensionada)
    fondo_label = tk.Label(ventana, image=imagen_fondo_tk)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    # función para redimensionar fondo
    def redimensionar_fondo(evento):
        nueva_imagen_pil = imagen_pil.resize((evento.width, evento.height), Image.LANCZOS)
        nueva_imagen_tk = ImageTk.PhotoImage(nueva_imagen_pil)
        fondo_label.config(image=nueva_imagen_tk)
        fondo_label.image = nueva_imagen_tk # Guardar referencia
    ventana.bind("<Configure>", redimensionar_fondo)

except FileNotFoundError:
    print(f"Advertencia: No se pudo cargar la imagen de fondo desde {ruta_imagen_fondo}")
    # Color de fondo alternativo si la imagen no carga
    ventana.configure(bg="#2E2E2E")
except Exception as e:
    print(f"Advertencia: Error al cargar la imagen de fondo: {e}")
    ventana.configure(bg="#2E2E2E")


# estilos / fuentes
font_visor_principal = ("Play", 32, "bold") # Para el display grande de "Total Cesantías"
font_visor_secundario = ("Play", 14) # Para los campos de entrada y el visor de subsidio
font_leyenda = ("Play", 15)# ESTE ES ESPECÍFICAMENTE PARA LAS LEYENDAS
font_boton_accion = ("Play", 12, "bold") # Para el botón "Hacer Cálculo"
font_boton_normal = ("Play", 10) # Para el botón "Ingresar SMLV"

color_fondo_visor = "black" # Color de fondo para los visores y entradas
color_texto_visor = "#00FF00" # Verde fosforescente
color_cursor_visor = "#00FF00"
relieve_visor = "sunken"
borde_visor = 2 # Más sutil

# Estilo para las leyendas descriptivas
estilo_leyenda_descriptiva = {
    'font': font_leyenda,
    'fg': 'white',        # Color de texto: BLANCO
    'bg': '#404040',      # Color de fondo: GRIS OSCURO (puedes probar otros como '#333333', 'dimgray')
    'anchor': "w"         # Mantenemos la alineación a la izquierda (west)
    # Puedes añadir 'padx': 5 si quieres un poco de espacio interno horizontal
}


# StringVars (Variables para controlar el texto de los widgets)
total_cesantias_var = tk.StringVar(value="0.00")
smlv_var = tk.StringVar()
dias_laborados_var = tk.StringVar()
subsidio_transporte_var = tk.StringVar(value="0.00") # Mostrará un valor calculado

# Configuración del Grid
# Columna 0 para botones/leyendas principales, Columna 1 para leyendas secundarias, Columna 2 para entradas/visores
ventana.columnconfigure(0, weight=0) # No se expande mucho (para botón SMLV y leyendas)
ventana.columnconfigure(1, weight=0) # No se expande mucho (para leyenda SMLV)
ventana.columnconfigure(2, weight=1) # Se expande (para la entrada SMLV y otras entradas que usan columnspan)


#<<<<<<<<<<<<LOGICA>>>>>>>>>>>>>>>>>
#dias
def manejar_calculo_en_gui():
    salario_texto = smlv_var.get()
    dias_texto = dias_laborados_var.get()

    try:
        # 1. Validar y convertir días laborados usando tu nueva función
        salario_texto_limpio = salario_texto.replace(',', '')
        dias_num_verificado = verificar_dia_entero(dias_texto) # Llamada a tu función importada

        if dias_num_verificado is None:
            # Si verificar_dia_entero devuelve None, el valor no es un entero válido
            total_cesantias_var.set("Error: Días debe ser un número entero.")
            subsidio_transporte_var.set("") # Limpiar otros campos si es necesario
            return # Salir de la función porque la entrada de días es incorrecta

        # 2. Convertir salario (usando el texto limpio)
        salario_num = float(salario_texto_limpio)

        # 3, Calcular Cesantías
        resultado_cesantias = calcular_cesantias_valor(salario_num, dias_num_verificado)

        # 4. Mostrar el resultado de Cesantías en la GUI
        total_cesantias_var.set(f"{resultado_cesantias:,.1f}")# Formateado para mostrar total cesantias

        # 5 Calcular y Mostrar Subsidio de Transporte
        monto_subsidio = calcular_monto_subsidio(salario_num)  # Llamas a tu nueva función
        subsidio_transporte_var.set(f"{monto_subsidio:,.0f}")  # Muestras el monto del subsidio formateado

    except ValueError as e_val:
        # Este ValueError puede venir de: float(salario_texto) si el salario no es un número.
        # Las validaciones de negocio DENTRO de calcular_cesantias_valor _num es negativo, o dias_num_verificado está fuera del rango 0-360
        total_cesantias_var.set(f"Error: {e_val}")
        subsidio_transporte_var.set("") # Limpiar subsidio también
    except TypeError as e_type:  # Para capturar el TypeError de la validación de tipo en la lógica
        total_cesantias_var.set(f"Error de tipo: {e_type}")
        subsidio_transporte_var.set("")
    except Exception as e_inesperado:
        total_cesantias_var.set("Error inesperado en cálculo.")
        subsidio_transporte_var.set("")
        print(f"Error GUI: {e_inesperado}") # Para tu depuración

#<<<<<<<<<<<<LOGICA BOTON smlv>>>>>>>>>>>>>>>>>
def manejar_ingreso_smlv():
    # Obtener el valor SMLV predeterminado
    smlv_fijo = obtener_smlv_predeterminado()

    # Verificar si el botón ya está deshabilitado (una forma de "solo una vez") O podrías verificar si el campo ya tiene ese valor específico.
    # Deshabilitar el botón es visualmente más claro para el usuario.
    if btn_ingresar_smlv['state'] == tk.DISABLED:
        print("SMLV ya fue ingresado mediante el botón.") # Mensaje para depuración
        return # No hacer nada más

    # Establecer el valor en el StringVar del campo de entrada SMLV Formateamos como un string que represente el número.
    smlv_var.set(f"{smlv_fijo:,.0f}") # ".0f" lo mostrará sin decimales 1423500 \ ",.0f"  mostrará "1,423,500"

    # Deshabilitar el botón después de usarlo una vez
    btn_ingresar_smlv.config(state=tk.DISABLED)
    print(f"SMLV predeterminado ({smlv_fijo}) ingresado. Botón deshabilitado.") # Mensaje para depuración

#<<<<<<<<<<<<LOGICA BOTON REINICIAR>>>>>>>>>>>>>>>>>
def reiniciar_campos_calculadora():
    # 1. Limpiar campos de entrada (StringVar)
    smlv_var.set("")
    dias_laborados_var.set("")

    # 2. Restablecer campos de resultado (StringVar)
    total_cesantias_var.set("0.00") # O el valor inicial que prefieras
    subsidio_transporte_var.set("0.00") # O el valor inicial que prefieras

    # 3. Re-habilitar el botón "Ingresar SMLV"
    #    Asumimos que btn_ingresar_smlv es el nombre de tu variable de botón
    if 'btn_ingresar_smlv' in globals() and btn_ingresar_smlv.winfo_exists():
        btn_ingresar_smlv.config(state=tk.NORMAL)
    else:
        # Esto es solo por si acaso, en tu código actual btn_ingresar_smlv debería existir
        print("Advertencia: No se pudo encontrar btn_ingresar_smlv para re-habilitarlo.")


    # 4. Opcional: Poner el foco en el primer campo de entrada
    #    Asumimos que entry_smlv es el nombre de tu widget de entrada para SMLV
    if 'entry_smlv' in globals() and entry_smlv.winfo_exists():
        entry_smlv.focus_set()

    print("Campos de la calculadora reiniciados.") # Mensaje para depuración

# --- Fila 0 y 1: Visor Principal "Total Cesantías" ---
# Leyenda para el visor principal
lbl_leyenda_total = tk.Label(ventana, text="Total Cesantías:", **estilo_leyenda_descriptiva)
lbl_leyenda_total.grid(row=0, column=0, columnspan=3, sticky="sw", padx=15, pady=(10, 0))

# Visor principal (Label estilizado)
visor_principal = tk.Label(
    ventana,
    textvariable=total_cesantias_var,
    font=font_visor_principal,
    bg=color_fondo_visor,
    fg=color_texto_visor,
    relief=relieve_visor,
    borderwidth=borde_visor+2, # Un poco más de borde para el principal
    anchor="e", # Alinea el texto a la derecha (East)
    padx=10,
    pady=5
)
visor_principal.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=(0, 20))

# Fila 2: Ingresar SMLV
# Botón "Ingresar SMLV"
btn_ingresar_smlv = tk.Button(
    ventana,
    text="Ingresar SMLV",
    font=font_boton_normal,
    command=manejar_ingreso_smlv
)
btn_ingresar_smlv.grid(row=2, column=0, sticky="ew", padx=(10, 5), pady=10)

# Leyenda para el visor de SMLV
lbl_leyenda_smlv = tk.Label(ventana, text="Salario Mínimo:", **estilo_leyenda_descriptiva)
lbl_leyenda_smlv.grid(row=2, column=1, sticky="w", padx=(0, 5), pady=10)

# Visor (Entry) para ingresar SMLV
entry_smlv = tk.Entry(
    ventana,
    textvariable=smlv_var,
    font=font_visor_secundario,
    bg=color_fondo_visor,
    fg=color_texto_visor,
    relief=relieve_visor,
    borderwidth=borde_visor,
    justify="right",
    insertbackground=color_cursor_visor # Color del cursor al escribir
)
entry_smlv.grid(row=2, column=2, sticky="ew", padx=(0, 10), pady=10)

# Fila 3: Ingresar Días Laborados
# Leyenda para el visor de días laborados
lbl_leyenda_dias = tk.Label(ventana, text="Ingrese días laborados:", **estilo_leyenda_descriptiva)
lbl_leyenda_dias.grid(row=3, column=0, sticky="w", padx=(10,5), pady=10)

# Visor (Entry) para ingresar días laborados
entry_dias = tk.Entry(
    ventana,
    textvariable=dias_laborados_var,
    font=font_visor_secundario,
    bg=color_fondo_visor,
    fg=color_texto_visor,
    relief=relieve_visor,
    borderwidth=borde_visor,
    justify="right",
    insertbackground=color_cursor_visor
)
# Este entry ocupará el espacio de la columna 2 para alinearse con el entry de SMLV
# Ajustamos para que la leyenda esté en col 0, y el entry en col 1 y 2 (span).
lbl_leyenda_dias.grid(row=3, column=0, sticky="w", padx=(10,5), pady=10) # Columna 0
entry_dias.grid(row=3, column=1, columnspan=2, sticky="ew", padx=(0,10), pady=10) # Columnas 1 y 2


# Fila 4: Mostrar Subsidio de Transporte
# Leyenda para el subsidio de transporte
lbl_leyenda_sub_transporte = tk.Label(ventana, text="Subsidio de Transporte:", **estilo_leyenda_descriptiva)
lbl_leyenda_sub_transporte.grid(row=4, column=0, sticky="w", padx=(10,5), pady=10)

# Visor (Label) para mostrar el subsidio (no editable)
visor_sub_transporte = tk.Label(
    ventana,
    textvariable=subsidio_transporte_var,
    font=font_visor_secundario,
    bg=color_fondo_visor,
    fg=color_texto_visor,
    relief=relieve_visor,
    borderwidth=borde_visor,
    anchor="e",
    padx=10
)
visor_sub_transporte.grid(row=4, column=1, columnspan=2, sticky="ew", padx=(0,10), pady=10)

# Fila 5: Botón de Cálculo
btn_hacer_calculo = tk.Button(
    ventana,
    text="Hacer Cálculo",
    font=font_boton_accion,
    bg="#4CAF50", # verde para el boton
    fg="white",
    relief="raised",
    borderwidth=2,
    padx=10,
    pady=5,
    command=manejar_calculo_en_gui, # Función a ejecutar al presionar el botón
)
btn_hacer_calculo.grid(row=5, column=0, columnspan=3, sticky="ew", padx=10, pady=(20, 10))

#Fila 6 : Botón de Reinicio
btn_reiniciar = tk.Button(
    ventana,
    text="\U0001F635", # Emoji "mareado" para borrar/reiniciar
    font=font_boton_accion,
    bg="#4CAF50", # verde para el boton
    fg="white",
    relief="raised",
    borderwidth=2,
    padx=20,
    pady=5,
    width=3,
    command=reiniciar_campos_calculadora # Conecta la función de reinicio
)
# para el grid
btn_reiniciar.grid(row=6, column=0, columnspan=3, sticky="ew", padx=10, pady=(10, 20))

# Ajustar el fondo de las etiquetas si no hay imagen de fondo
if not ruta_imagen_fondo or "Advertencia" in str(fondo_label): # Si no se cargó el fondo
    for widget in [lbl_leyenda_total, lbl_leyenda_smlv, lbl_leyenda_dias, lbl_leyenda_sub_transporte]:
        widget.config(bg="#2E2E2E", fg="white") # Fondo oscuro, texto claro

#Bucle Principal
ventana.mainloop()