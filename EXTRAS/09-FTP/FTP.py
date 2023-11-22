#Francisco Abbadv Ramirez Gomez
#1872531
#Script para transferencia de ftp
from ftplib import FTP
nuevo_archivo=r"C:\Users\luisc\Downloads\Fr\ADVERTENCIA.v2.txt"
# Establecer conexion FTP
ftp = FTP('192.168.138.129')
ftp.login('francisco', '1872531')

# Cambiar al directorio 'upload'
ftp.cwd('upload')

# Listar archivos en el directorio actual
ftp.retrlines('LIST')

# Subir el archivo al servidor FTP usando storbinary
with open(nuevo_archivo, 'rb') as archivo:
    ftp.storbinary(f'STOR ADVERTENCIA.txt', archivo)

# Cerrar la conexion FTP
ftp.quit()
