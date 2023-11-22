# Limpiando pantalla
#
Clear-Host
#
# Mensaje de bienvenida
#
Write-Host "Ejemplo de codificador Base64 en Powershell" -ForegroundColor Yellow
#
# Mnesje codificado en Base64
#
$texto = 'TABhAGIAbwByAGEAdABvAHIAaQBvACAAZABlACAAUAByAG8AZwByAGEAbQBhAGMAaQDzAG4AIABwAGEAcgBhACAAQwBpAGIAZQByAFMAZQBnAHUAcgBpAGQAYQBkACAAUwBlAHMAaQDzAG4AIAAxADAA'
Write-Host " La cadena a decodificar es: "
Write-Host $texto
#
# Decodificando mensaje
#
$decod = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($texto))
Write-Host "La cadena ya decodificada es: " -ForegroundColor Green
Write-Host $decod