import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    while True:
        message = input("Ingrese mensaje: ")
        client.sendall(message.encode())
        response = client.recv(1024)
        if message.upper() == "DESCONEXION":
            break
        print("Respuesta del servidor:", response.decode())