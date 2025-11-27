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

