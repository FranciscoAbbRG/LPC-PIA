#!/bin/bash
# Script para listar procesos ejecutándose en el servidor

# Variables
TIME=$(date +%d-%m-%Y_%H:%M:%S)
FECHA=$(date +%d-%m-%Y)

# Creando directorio log
if [ ! -d "$HOME/log" ]; then
    mkdir "$HOME/log"
fi

# Listando procesos
echo -e "######################################\n"\
        "#\n"\
        "# Hora: $TIME\n"\
        "######################################\n"\
        "#" >> "$HOME/log/procesos_${FECHA}.log"

ps -ef >> "$HOME/log/procesos_${FECHA}.log"

echo -e "TOTAL DE PROCESOS: $(ps -ef | wc -l)\n"\
        "Hora: $TIME" >> "$HOME/log/procesos_${FECHA}.log"

