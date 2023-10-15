from modelo.datosMeteorologicos import DatosMeteorologicos

datos = DatosMeteorologicos("datos.txt")
print(datos.procesar_datos())