# kosmos-server-client
## Servidor y Cliente TCP en Python

### Requisitos
- Python 3 instalado en tu sistema.

### Instalación
1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener Python instalado.

### Ejecución
#### Servidor
Ejecuta el servidor con:
```sh
python src/server.py
```
Esto iniciará el servidor en `localhost:65432`.

#### Cliente
En otra terminal, ejecuta el cliente con:
```sh
python src/client.py
```
Ingresa mensajes en la terminal del cliente

### Pruebas Manuales
1. Enviar un mensaje de prueba (ejemplo: `hola`), el servidor debe responder `HOLA`.
2. Enviar `DESCONEXION`, el cliente y el servidor deben cerrar la conexión correctamente.