#Francisco Abbad Ramirez Gomez
#1872531

import nmap

# Función para mostrar el menú principal
def menu():
    print("1. Escaneo UDP")
    print("2. Escaneo Completo")
    print("3. Detección de Sistema Operativo")
    print("4. Escaneo de Red con Ping")
    print("5. Salir")

# Programa principal
if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "0":
            break
        elif opcion == "1":
            host = input("Ingrese la dirección IP del host: ")
            escaner = nmap.PortScanner()
            escaner.scan(host, arguments='-sU')
            print("Resultados del escaneo UDP:")
            for host, resultado in escaner.all_hosts().items():
                 print(f"Host: {host}")
                 for puerto, info in resultado['udp'].items():
                    print(f"Puerto {puerto}: {info['state']} - {info['name']}")
        elif opcion == "2":
            host = input("Ingrese la dirección IP del host: ")
            escaner = nmap.PortScanner()
            escaner.scan(host, arguments='-p- -sV')
            for scanned_host in escaner.all_hosts():
                print(f"Host: {scanned_host}")
                if 'tcp' in escaner[scanned_host]:
                    for puerto, info in escaner[scanned_host]['tcp'].items():
                        print(f"Puerto {puerto}: {info.get('state', 'Desconocido')} - {info.get('name', 'Desconocido')} - {info.get('product', 'Desconocido')} {info.get('version', 'Desconocido')}")
        elif opcion == "3":
            host = input("Ingrese la dirección IP del host: ")
            escaner = nmap.PortScanner()
            escaner.scan(host, arguments='-O')
            print(f"Sistema Operativo de {host}: {escaner[host]['osmatch'][0]['name']}")
        elif opcion == "4":
            red = input("Ingrese la dirección de red (por ejemplo, 192.168.1.0/24): ")
            escaner = nmap.PortScanner()
            escaner.scan(hosts=red, arguments='-sn')
            for host in escaner.all_hosts():
                print(f"Host: {host} está activo (respondió al ping)")
        else:
            print("Opción no válida. Favor de seleccionar una opcion valida.")
