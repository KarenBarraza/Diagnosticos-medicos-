import csv
from csv import DictWriter


class GestionarArchivo:
    def __init__(self):
        pass

    def leer_datos(self, ruta):
        filas = []
        with open(ruta, encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                filas.append(fila)
        return filas

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