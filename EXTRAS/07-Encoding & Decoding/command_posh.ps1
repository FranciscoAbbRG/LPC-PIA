#
# Comando de powershell a codificar en base64
#
$comando = 'Get-WmiObject win32_logicaldisk │ foreach (Write-Host $_.deviceID $_.size $_.freespace)'
#
# codificando $comando
#
$encode = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($comando))
Write-Host $encode
#
# Ejecutando el comando codificado
#
Write-Host "Vamos a ejecutar el comando asi: powershell -E" $encode -ForegroundColor Cyan
Start-Sleep 1
powershell -E $encode
#
Start-Sleep 2
#
# $comando_secret guarda un comando codificando en Base64
#
$comando_secret=''
#
# Decodificamos el comando
#
$decod = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($comando_secret))
#
## Mostramos el resultado
#
Write-Host "El comando codificado es:" -ForegroundColor Cyan
Write-Host $comando_secret
Write-Output ""
Write-Host "El comando ya sin codificar:" -ForegroundColor Cyan
Write-Host $decod