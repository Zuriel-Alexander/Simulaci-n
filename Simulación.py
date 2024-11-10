import tkinter as tk
from PIL import Image, ImageTk
import serial  # Comunicar con Arduino
import time

# Configuración de conexión serial
arduino = serial.Serial('COM3', 9600)  # Cambia 'COM3' al puerto serial de tu Arduino
time.sleep(2)  # Espera a que se inicie la conexión

# Funciones de cambio de estado de la puerta
def abrir_puerta():
    img_puerta = ImageTk.PhotoImage(Image.open("puerta_abierta.jpg"))
    lbl_imagen.config(image=img_puerta)
    lbl_imagen.image = img_puerta

def cerrar_puerta():
    img_puerta = ImageTk.PhotoImage(Image.open("puerta_cerrada.jpg"))
    lbl_imagen.config(image=img_puerta)
    lbl_imagen.image = img_puerta

# Función para verificar acceso con Arduino
def verificar_acceso():
    if arduino.in_waiting > 0:
        mensaje = arduino.readline().decode().strip()
        if mensaje == "acceso permitido":
            abrir_puerta()
        elif mensaje == "acceso denegado":
            cerrar_puerta()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Simulación de Acceso por Huella Digital")
ventana.geometry("400x600")
ventana.resizable(False, False)

# Imagen inicial (puerta cerrada)
img_puerta = ImageTk.PhotoImage(Image.open("puerta_cerrada.jpg"))
lbl_imagen = tk.Label(ventana, image=img_puerta)
lbl_imagen.pack()

# Llama a `verificar_acceso` cada segundo para verificar el mensaje de Arduino
def actualizar_estado():
    verificar_acceso()
    ventana.after(1000, actualizar_estado)

# Iniciar la verificación en intervalos
actualizar_estado()

# Iniciar la ventana
ventana.mainloop()