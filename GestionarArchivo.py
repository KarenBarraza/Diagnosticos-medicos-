#Se importa el archivo csv a utilizar
import csv
#Desde el archivo csv se importa una libreria que logra correr el codigo
from csv import DictWriter

#Se crea una clase por constructor para gestionar el archivo 
class GestionarArchivo:
#Se crea un init para crear un objeto
    def __init__(self):
        pass
#Se realiza una funcion para leer el archivo con filas
    def leer_datos(self, ruta):# -> recibe la ruta del archivo
        filas = []
        with open(ruta, encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                filas.append(fila)
        return filas
#Funcion para crear el archivo csv limpio
    def escribir_csv(self,ruta, datos, fieldnames=None):
        if not datos:
            print("No hay filas para escribir.")
            return
        if fieldnames is None:
            fieldnames = list(datos[0].keys())
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            for fila in datos:
                limpia = {k: ("" if v is None else v) for k, v in fila.items()}
                writer.writerow(limpia)
        print(f"Archivo guardado correctamente en: {ruta}")
