#!/bin/bash

# Función para escanear una red
escanear_red() {
    echo "Introduce la red a escanear (por ejemplo, 192.168.1.0/24):"
    read network
    echo "Escaneando la red $network..."
    sudo nmap $network
}

# Función para escanear una IP
escanear_ip() {
    echo "Introduce la IP a escanear:"
    read ip
    echo "Escaneando la IP $ip..."
    sudo nmap $ip
}

# Función para escanear UDP
escanear_udp() {
    echo "Introduce la IP o rango de IPs a escanear:"
    read target
    echo "Escaneando puertos UDP en $target..."
    sudo nmap -sU $target
}

# Función para escanear con scripts
escanear_con_scripts() {
    echo "Introduce la IP o rango de IPs a escanear con scripts:"
    read target
    echo "Escaneando con scripts en $target..."
    sudo nmap -sC $target
}

# Menú principal
while true; do
    echo "Selecciona una opción:"
    echo "1. Escanear una red"
    echo "2. Escanear una IP"
    echo "3. Escanear UDP"
    echo "4. Escanear con scripts"
    echo "5. Salir"

    read opcion

    case $opcion in
        1) escanear_red ;;
        2) escanear_ip ;;
        3) escanear_udp ;;
        4) escanear_con_scripts ;;
        5) echo "Saliendo del programa"; exit 0 ;;
        *) echo "Opción no válida. Por favor, selecciona una opción del 1 al 5." ;;
    esac
done
