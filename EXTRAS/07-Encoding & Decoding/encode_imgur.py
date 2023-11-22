import requests # Para hacer un resquest a un sitio
import base64 #Para Encode/decode en base 64
from requests import Respone
#
## Para descargar la imagen del sitio
#
if__name__=='__main__':
   url = 'https://imgur.com/gallery/ZeqHHQ1'

   Response: Response = requests.get(url, stream=True)
   with open('stones.jpg','wb') as file_down:
       for chunk in Response.iter_content(): # Descargando contenido poco a poco.
           file_down.write(chunk)
   Response.close()
#
## Para codificar la imagen
#
with open('stones.jpg','rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    base64_messsage = base64_endoded_data.decode('utf8')

    print (base64_messsage)

#Francisco Abbad Ramírez Gómez
#1872531