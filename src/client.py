import socket
import hashlib

# Definir la dirección IP y puerto del servidor (en local usamos loopback)
HOST = '10.20.38.137'
PORT = 65432

def compute_hash(password: str) -> str:
    """Calcula el hash SHA-256 de la contraseña."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def iniciar_cliente():
    # Solicitar la contraseña al usuario
    password_attempt = input("Introduce la contraseña: ")
    hashed_password = compute_hash(password_attempt)
    print(f"[+] Hash calculado: {hashed_password}")

    # Crear un socket TCP/IP y conectar al servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        # Enviar el hash de la contraseña
        client_socket.sendall(hashed_password.encode('utf-8'))

        # Esperar la respuesta del servidor
        response = client_socket.recv(1024)
        print("Respuesta del servidor:", response.decode('utf-8'))

if __name__ == '__main__':
    iniciar_cliente()

