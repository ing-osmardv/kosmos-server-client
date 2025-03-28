import socket

def run_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        
        print(f"Servidor TCP escuchando en {host}:{port} (Ctrl+C para detener)")

        try:
            while True:
                conn, addr = server_socket.accept()
                print(f"\nConexión establecida desde {addr[0]}:{addr[1]}")
                
                try:
                    handle_client_connection(conn, addr)
                except (ConnectionError, UnicodeDecodeError) as e:
                    print(f"Error con cliente {addr}: {str(e)}")
                finally:
                    conn.close()
                    print(f"Conexión cerrada con {addr[0]}:{addr[1]}")
                    
        except KeyboardInterrupt:
            print("\nServidor detenido por el usuario")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

def handle_client_connection(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
            
        try:
            message = data.decode('utf-8').strip()
            print(f"[{addr[0]}:{addr[1]}] Mensaje recibido: {message}")
            
            if message.upper() == "DESCONEXION":
                print(f"Cliente {addr[0]}:{addr[1]} solicitó desconexión")
                conn.sendall("ACK_DESCONEXION".encode('utf-8'))
                break
                
            response = message.upper()
            conn.sendall(response.encode('utf-8'))
            
        except UnicodeDecodeError:
            conn.sendall("ERROR: Mensaje no válido (UTF-8 requerido)".encode('utf-8'))
            continue

if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 65432
    
    run_server(HOST, PORT)