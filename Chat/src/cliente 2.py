import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

# Configuración del servidor
HOST = '127.0.0.1'  # Cambia esto si es necesario
PORT = 12345  # El mismo puerto que el servidor

# Función que se ejecuta cuando se presiona el botón de "Enviar"
def enviar_mensaje():
    mensaje = entrada_texto.get()  # Obtener el texto del campo de entrada
    if mensaje:
        area_chat.insert(tk.END, "Tú: " + mensaje + "\n")  # Mostrar el mensaje en el área de chat
        entrada_texto.delete(0, tk.END)  # Limpiar el campo de entrada después de enviar el mensaje
        # Enviar el mensaje al servidor
        try:
            cliente_socket.sendall(mensaje.encode('utf-8'))
        except Exception as e:
            area_chat.insert(tk.END, f"[ERROR] No se pudo enviar el mensaje: {e}\n")

# Función para recibir mensajes del servidor
def recibir_mensajes():
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode('utf-8')
            if mensaje:
                area_chat.insert(tk.END, mensaje + "\n")  # Mostrar el mensaje en el área de chat
        except Exception as e:
            area_chat.insert(tk.END, f"[ERROR] No se pudo recibir el mensaje: {e}\n")
            break

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Chat Simple con Tkinter")

# Crear el área de texto para mostrar los mensajes del chat
area_chat = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=50, height=15, state='normal')
area_chat.pack(padx=10, pady=10)

# Crear un marco (frame) para el campo de entrada y el botón
frame_inferior = tk.Frame(ventana)
frame_inferior.pack(pady=10)

# Crear el campo de entrada para escribir el mensaje
entrada_texto = tk.Entry(frame_inferior, width=60)
entrada_texto.pack(side=tk.LEFT, padx=10)

# Crear el botón de "Enviar"
boton_enviar = tk.Button(frame_inferior, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(side=tk.LEFT)

# Crear el socket del cliente
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Intentar conectarse al servidor
try:
    cliente_socket.connect((HOST, PORT))
    area_chat.insert(tk.END, "[CONEXIÓN EXITOSA] Conectado al servidor.\n")
except Exception as e:
    area_chat.insert(tk.END, f"[ERROR DE CONEXIÓN] No se pudo conectar al servidor: {e}\n")

# Iniciar un hilo para recibir mensajes del servidor
hilo_recibir = threading.Thread(target=recibir_mensajes)
hilo_recibir.daemon = True  # Permitir que el hilo se cierre al cerrar la ventana
hilo_recibir.start()

# Ejecutar el bucle principal de Tkinter
ventana.mainloop()

# Cerrar el socket al cerrar la ventana
cliente_socket.close()
