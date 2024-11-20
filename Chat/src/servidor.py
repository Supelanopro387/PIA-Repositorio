import socket
import threading

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP del servidor (localhost)
PORT = 12345        # Puerto para escuchar conexiones

# Lista para almacenar clientes conectados
clientes_conectados = []


# Función para manejar a cada cliente conectado
def manejar_cliente(conn, addr):
    print(f"[NUEVA CONEXIÓN] {addr} conectado.")
    clientes_conectados.append(conn)

    conectado = True
    while conectado:
        try:
            # Recibir el mensaje del cliente
            mensaje = conn.recv(1024).decode('utf-8')
            if mensaje:
                print(f"[{addr}] {mensaje}")  # Mostrar mensaje en la consola 
                # Reenviar el mensaje a todos los clientes conectados
                enviar_a_todos(f"[{addr}] {mensaje}", conn)
            else:
                conectado = False
        except ConnectionResetError:
            conectado = False
        except Exception as e:
            print(f"[ERROR] Ocurrió un error: {e}")
            conectado = False

    # Eliminar cliente desconectado
    conn.close()
    clientes_conectados.remove(conn)
    print(f"[DESCONECTADO] {addr} desconectado.")


# Función para enviar mensajes a todos los clientes conectados
def enviar_a_todos(mensaje, cliente_actual):
    for cliente in clientes_conectados:
        if cliente != cliente_actual:
            try:
                cliente.send(mensaje.encode('utf-8'))
            except Exception as e:
                print(
                    "[ERROR EN ENVÍO] Ocurrió un error al enviar a un cliente: "
                    f"{e}"
                )
                cliente.close()
                clientes_conectados.remove(cliente)


# Función para iniciar el servidor
def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"[INICIANDO] Servidor escuchando en {HOST}:{PORT}")

    while True:
        conn, addr = servidor.accept()
        hilo_cliente = threading.Thread(
            target=manejar_cliente,
            args=(conn, addr)
        )
        hilo_cliente.start()
        print(f"[CONEXIONES ACTIVAS] {threading.active_count() - 1}")


# Iniciar el servidor
print("[INICIANDO] Iniciando servidor...")
iniciar_servidor()
