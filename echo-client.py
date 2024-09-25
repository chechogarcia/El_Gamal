#!/usr/bin/env python3

import socket
import el_gamal

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

priv_alice = 20

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    mensaje = el_gamal.letter_ascii(input("Ingrese el texto que quiere mandar: "))

    data = s.recv(1024)
    print(data)

    lista = list(str(data).split())

    

    llave_publica = lista[10:13]
    for x in range(3):
        nuevo_x = ""
        for y in range(len(llave_publica[x])):
            if llave_publica[x][y]!="'" and llave_publica[x][y] != "," and llave_publica[x][y]!="(" and llave_publica[x][y]!=")":
                nuevo_x += llave_publica[x][y]
        llave_publica[x] = int(nuevo_x)
    

    mensaje_cifrado = el_gamal.el_gamal_encrip(mensaje, llave_publica)

    print(mensaje_cifrado)

    firma = el_gamal.firma(mensaje, llave_publica, priv_alice)

    tupla_mensaje = []
    tupla_mensaje.append(mensaje_cifrado[0])
    tupla_mensaje.append(mensaje_cifrado[1])
    tupla_mensaje.append(firma)
    
    s.sendall(bytes(str(tupla_mensaje), 'utf-8'))
