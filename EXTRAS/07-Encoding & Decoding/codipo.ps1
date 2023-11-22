Clear-Host
Write-Host "Bienvenido a un ejemplo de codificacion / decodificacion base64 usando powershell" -ForegroundColor Green
Write-Host "Codificando un archivo de texto"
#
# Se va a leer el contenido del archivo de texto
#
$inputfile = ""
$fc = Get-Content $inputfile
$GB = [System.Text.Encoding]::UTF8.GetBytes($fc)
$etext = [System.Convert]::ToBase64String($GB)
Write-Host "El contenido del archivo CODIFICADO es:" $etext -ForegroundColor Green 
#
# Decodificando contenido de un archivo
#
Write-Host "DECODIFICANDO el texto previo:"
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($etext)) │ out-file -Encoding "ASCII" C:
$outfile12 = Get-Content c:
Write-Host "El texto decodificado es el siguiente:" -ForegroundColor Green
Write-Host "DECODIFICADO:" $outfile12