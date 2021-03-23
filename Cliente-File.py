# -*- coding: utf-8 -*-

# Envio de archivos: cliente
# 11Sep

import socket

# Creamos una lista con la dirección de
# la máquina y el puerto donde
# estara a la escucha
CONEXION = ('ia', 5000)
ARCHIVO = "prueba.txt"


# Instanciamos el socket y nos
# conectamos
cliente = socket.socket()
cliente.connect(CONEXION)
print("conectado al servidor")

# Abrimos el archivo en modo lectura binaria
# y leemos su contenido
with open(ARCHIVO, "rb") as archivo:
    buffer = archivo.read()

print("archivo abierto")

while True:
    # Enviamos al servidor la cantidad de bytes
    # del archivo que queremos enviar
    tamanio = str(len(buffer))
    cliente.send(tamanio.encode("ascii"))
   
    # Esperamos la respuesta del servidor
    recibido = cliente.recv(10)
    if recibido == "OK":
        # En el caso que la respuesta sea la correcta
        # enviamos el archivo byte por byte
        # y salimos del while
        for byte in buffer:
            cliente.send(byte)
        break
