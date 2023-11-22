#Francisco Abbad Ramirez Gomez
#1872531

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Configura los detalles del mensaje
remite = "frankyfcfm@gmail.com"
destinatario = "francisco.ramirezgz@uanl.edu.mx"
asunto = "Practica12"

# Crea el objeto MIMEText con el contenido en formato HTML
mensaje_html = """
<p class="demoTitle">&nbsp; &nbsp; &nbsp;<span style="color: #000000;">"Practica 12</span></p>
<p class="demoTitle"><span style="color: #000000;">Ejercicio de la practica 12 para env&iacute;o de correos</span></p>
<p class="demoTitle"><span style="color: #000000;">Alumno: Francisco Abbad Ram&iacute;rez G&oacute;mez</span></p>
<p class="demoTitle"><span style="color: #000000;">Matricula: 1872531</span></p>
<p class="demoTitle"><span style="color: #000000;">"</span></p>
<p class="demoTitle">&nbsp;</p>
<!-- Comments are visible in the HTML source only -->
"""

msg = MIMEMultipart()
msg["From"] = remite
msg["To"] = destinatario
msg["Subject"] = asunto

mensaje = MIMEText(mensaje_html, "html")
msg.attach(mensaje)

# Anexa la imagen
with open("C:/Users/prueba/Desktop/practica12/fcfm_cool.png", "rb") as file:   #Poner la ruta del archivo
    imagen = MIMEImage(file.read(), name="fcfm_cool.png")
    imagen.add_header("Content-ID", "<imagen_anexa>")
    msg.attach(imagen)

try:
    # Conecta al servidor SMTP (en este caso, se utiliza Gmail)
    conn = smtplib.SMTP("smtp.gmail.com", 587)
    conn.starttls()
    conn.login("frankyfcfm@gmail.com", "contraseña") #Dato sensible, poner la contraseña de la aplicación

    # Envía el correo
    conn.sendmail(remite, destinatario, msg.as_string())
    conn.quit()

    print("Correo HTML con imagen enviado con éxito")
except Exception as e:
    print("Ocurrió un error al enviar el correo:", str(e))
