import requests
import json
#
if __name__ == "__main__":
    url = "https://httpbin.org/post"
    argumentos = {"nombre":"Francisco Abbad Ramirez Gomez","matricula":"1872531","curso":"Programacion para ciberseguridad"}

    response = requests.post(url, params=argumentos)

    if response.status_code == 200:
        print(response.content)