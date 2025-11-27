from GestionarArchivo import GestionarArchivo
from NormalizacionDatos import NormalizacionDatos
import csv

gestor = GestionarArchivo()
filas = gestor.leer_datos("dataset5_patient_diagnoses.csv")  

procesador = NormalizacionDatos(columna="patient_id", inicio=1001)
filas = procesador.renumerar_ids(filas)

for fila in filas[:110]:
    print(fila)
