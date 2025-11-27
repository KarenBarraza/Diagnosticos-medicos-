from GestionarArchivo import GestionarArchivo
from datetime import datetime
           
class NormalizacionDatos:
    def __init__(self, datos):
        self.datos = datos
        self.limpiar_diagnosticos()
    
    def MostrarListado(self,datos):
        for lista in datos:
            print(lista)
            
    def normalizar_texto(self, texto):
        if not texto:
            return ""
        # Convierte todo a minúscula y luego la primera letra a mayúscula
        return texto.lower().capitalize()

    def limpiar_diagnosticos(self):
        for fila in self.datos:
            fila["diagnosis"] = self.normalizar_texto(fila.get("diagnosis", ""))
            fila["diagnosis_group"] = self.normalizar_texto(fila.get("diagnosis_group", ""))


        
            