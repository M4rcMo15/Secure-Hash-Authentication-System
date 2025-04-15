import socket

# Definición del hash correcto de la contraseña (SHA-256 de la contraseña "passw0rd")
CORRECT_HASH = "807c6d83b02cb8422209460568b729356c4cb3d3b38a803a7b0fd55b47916db9"

# Definición de la dirección IP y puerto a usar (loopback y un puerto no privilegiado)
HOST = '10.20.38.137'
PORT = 65432

def iniciar_servidor():
    # Crear un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"[+] Servidor escuchando en {HOST}:{PORT}")

        while True:
            # Espera una conexión
            conn, addr = server_socket.accept()
            with conn:
                print(f"[+] Conexión establecida desde: {addr}")

                # Recibir datos enviados por el cliente
                data = conn.recv(1024)
                if not data:
                    print("[-] No se recibieron datos.")
                    continue

                # Convertir los datos recibidos de bytes a string y limpiar espacios
                received_hash = data.decode('utf-8').strip()
                print(f"[+] Hash recibido: {received_hash}")

                # Comprobar si el hash recibido coincide con el hash correcto
                if received_hash == CORRECT_HASH:
                    response = "[+] Login exitoso"
                else:
                    response = "[!] Login fallido"

                # Enviar respuesta al cliente
                conn.sendall(response.encode('utf-8'))
                print(f"[+] Respuesta enviada: {response}\n")

if __name__ == '__main__':
    iniciar_servidor()

