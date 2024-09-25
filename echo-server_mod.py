#!/usr/bin/env python3

import socket
import el_gamal

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

p = int(input("Ingrese el primo que va a usar: "))
alpha = int(input("Ingrese el alpha que va a usar: "))
d = int(
  input("Escoja su clave privada (debe ser un entero entre 2 y " + str(p - 1) +
        "): "))

primo_alice = 16136133237524628623079973436761666157812135802554422133884399716278215827708188540430994158743163224360474004390260851035079396569070805436204141716645377206469931168305351122258807934047024235765278566582937247825531441295648260124631056178986340098086793666788683120626019654875802245983332214723863553333

llave_pubica_alice = el_gamal.gen_llave_publica(20, 5, primo_alice)

while True:
  if d == 1 or d >= p - 1:
    print("Esa clave no es valida...")
    d = int(
      input("Escoja su clave privada (debe ser un entero entre 2 y " +
            str(p - 1) + "): "))
  else:
    break

llave_publica = el_gamal.el_gamal_gen_llave_publica(d, alpha, p)
print("Tu llave publica es " + str(llave_publica))
print("")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept()
  with conn:
    print(f"Connectado con {addr}")

    conn.sendall(b"Hola! Si quieres mandarme un mensaje usa mi llave publica ")
    llave_mandar = bytes(str(llave_publica), 'utf-8')

    conn.send(llave_mandar)

    while True:
      data = conn.recv(1024)
      if not data:
        break
      print("")
      conn.sendall(b"Mensaje recibido!")
      print("El mensaje cifrado es: ")
      print(data)

      texto_cifrado = list(str(data).split())

      print("")

      for x in range(2):
        nuevo_x = ""
        for y in range(len(texto_cifrado[x])):
          if texto_cifrado[x][y] != "'" and texto_cifrado[x][
              y] != "," and texto_cifrado[x][y] != "(" and texto_cifrado[x][
                y] != ")" and texto_cifrado[x][y] != "b":
            nuevo_x += texto_cifrado[x][y]
        texto_cifrado[x] = int(nuevo_x)

      texto_claro = el_gamal.el_gamal_decrip(texto_cifrado, p, d)

      for x in range(2):
        nuevo_x = ""
        for y in range(len(texto_cifrado[x+2])):
          if texto_cifrado[x+2][y] != "'" and texto_cifrado[x+2][
              y] != "," and texto_cifrado[x+2][y] != "(" and texto_cifrado[x+2][
                y] != ")" and texto_cifrado[x+2][y] != "b":
            nuevo_x += texto_cifrado[x+2][y]
        texto_cifrado[x+2] = int(nuevo_x)

      print("El texto claro es: " + el_gamal.ascii_letter(texto_claro))

      el_gamal.comprobacion_firma(texto_cifrado, llave_pubica_alice,
                                  texto_claro)

      s.close()
