@echo off

:: Definir la nueva ruta
set "newPath=C:\WinSLO"

setx /M PATH "%PATH%;%newPath%"
