#Francisco Abbad Ramírez Gómez
#1872531
import base64
#
# obtendremos una frase dessde el input principal.
#
print ("Bienvenido a codificadorBase64 en Python")
frase = input("Proporciona una frase para codificar: ")
#
# obtendremos los bytes de la frase
#
frase_bytes = frase.encode('ascii')
#
# Se calculan los bytes de la base64
#
base64_bytes = base64.b64encode(frase_bytes)
#
#
#
base64_message = base64_bytes.decode('ascii')
print("La frase codificada en base 64 es: ")
print(base64_message)