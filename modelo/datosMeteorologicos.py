class DatosMeteorologicos:
    
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo
    
    
    def procesar_datos(self)-> tuple[float, float, float, float, str]:
        t_temperatura = []
        t_humedad = []
        t_presion = []
        t_velocidad_viento = []
        t_direccion_viento = []
        
        with open(self.nombre_archivo, 'r', encoding="utf-8") as archivo:
            datos = archivo.read().split("\n\n")
            for estacion in datos:
                lineas = estacion.split("\n")
                for linea in lineas:
                    if "Temperatura" in linea:
                        temperatura = float(linea.split(": ")[1])
                        t_temperatura.append(temperatura)
                    
                    elif "Humedad" in linea:
                        humedad = float(linea.split(": ")[1])
                        t_humedad.append(humedad)
                        
                    elif "Presion" in linea:
                        presion = float(linea.split(": ")[1])
                        t_presion.append(presion)
                        
                    elif "Viento" in linea:
                        dato_viento = linea.split(": ")[1]
                        velocidad = float(dato_viento.split(",")[0])
                        t_velocidad_viento.append(velocidad)
                        
                        direccion = dato_viento.split(",")[1]
                        if direccion == "N":
                            t_direccion_viento.append(0)
                        elif direccion == "NNE":
                            t_direccion_viento.append(22.5)
                        elif direccion == "NE":
                            t_direccion_viento.append(45)
                        elif direccion == "E":
                            t_direccion_viento.append(90)
                        elif direccion == "ESE":
                            t_direccion_viento.append(112.5)
                        elif direccion == "SE":
                            t_direccion_viento.append(135)
                        elif direccion == "SSE":
                            t_direccion_viento.append(157.5)
                        elif direccion == "S":
                            t_direccion_viento.append(180)
                        elif direccion == "SSW":
                            t_direccion_viento.append(202.5)
                        elif direccion == "SW":
                            t_direccion_viento.append(225)
                        elif direccion == "WSW":
                            t_direccion_viento.append(247.5)
                        elif direccion == "W":
                            t_direccion_viento.append(270)
                        elif direccion == "WNW":
                            t_direccion_viento.append(292.5)
                        elif direccion == "NW":
                            t_direccion_viento.append(315)
                        elif direccion == "NNW":
                            t_direccion_viento.append(337.5)
                            
        prom_temperatura = sum(t_temperatura) / len(t_temperatura)
        prom_humedad = sum(t_humedad) / len(t_humedad)
        prom_presion = sum(t_presion) / len(t_presion)
        prom_viento = sum(t_velocidad_viento) / len(t_velocidad_viento)
        prom_dir_viento = sum(t_direccion_viento) / len(t_direccion_viento)
        
        def clasificar_direccion():
            if 0 <= prom_dir_viento < 22.5 or 360 == prom_dir_viento:
                return "N"
            elif 22.5 <= prom_dir_viento < 45:
                return "NNE"
            elif 45 <= prom_dir_viento < 67.5:
                return "NE"
            elif 67.5 <= prom_dir_viento < 90:
                return "ENE"
            elif 90 <= prom_dir_viento < 112.5:
                return "E"
            elif 112.5 <= prom_dir_viento < 135:
                return "ESE"
            elif 135 <= prom_dir_viento < 157.5:
                return "SE"
            elif 157.5 <= prom_dir_viento < 180:
                return "SSE"
            elif 180 <= prom_dir_viento < 202.5:
                return "S"
            elif 202.5 <= prom_dir_viento < 225:
                return "SSW"
            elif 225 <= prom_dir_viento < 247.5:
                return "SW"
            elif 247.5 <= prom_dir_viento < 270:
                return "WSW"
            elif 270 <= prom_dir_viento < 292.5:
                return "W"
            elif 292.5 <= prom_dir_viento < 315:
                return "WNW"
            elif 315 <= prom_dir_viento < 337.5:
                return "NW"
            elif 337.5 <= prom_dir_viento < 360:
                return "NNW"
        
        return (prom_temperatura, prom_humedad, prom_presion, prom_viento, clasificar_direccion())