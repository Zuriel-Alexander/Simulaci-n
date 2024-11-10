import tkinter as tk
from PIL import Image, ImageTk
import time
import serial  # Para simular la comunicación con Arduino, aunque no se use directamente

# Configuración de ventana
ventana = tk.Tk()
ventana.title("Simulación de Acceso")
ventana.geometry("400x600")  # Tamaño fijo de ventana
ventana.resizable(False, False)

# Cargar imágenes de la puerta
puerta_cerrada = ImageTk.PhotoImage(Image.open("puerta_cerrada.png"))
puerta_abierta = ImageTk.PhotoImage(Image.open("puerta_abierta.png"))

# Etiqueta para mostrar la imagen
etiqueta_puerta = tk.Label(ventana, image=puerta_cerrada)
etiqueta_puerta.pack()


# Función para verificar acceso del usuario
def verificar_acceso():
    # Aquí podrías colocar la lógica para verificar huella
    # Simularemos un proceso de verificación
    tiene_acceso = True  # Cambiar a `False` para simular acceso denegado

    # Cambiar imagen de acuerdo a si tiene o no acceso
    if tiene_acceso:
        etiqueta_puerta.config(image=puerta_abierta)
        ventana.update()
        time.sleep(2)  # Mantener la puerta abierta por 2 segundos
        etiqueta_puerta.config(image=puerta_cerrada)  # Regresar a puerta cerrada
    else:
        etiqueta_puerta.config(image=puerta_cerrada)
        ventana.update()


# Botón para iniciar la verificación
boton_acceso = tk.Button(ventana, text="Verificar Huella", command=verificar_acceso)
boton_acceso.pack(pady=20)

# Iniciar el bucle principal
ventana.mainloop()