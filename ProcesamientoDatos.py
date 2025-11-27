from GestionarArchivo import GestionarArchivo
from NormalizacionDatos import NormalizacionDatos

gestor = GestionarArchivo()
datos = gestor.leer_datos("dataset5_patient_diagnoses.csv")

normalizacion = NormalizacionDatos(datos)
normalizacion.MostrarListado(n=10)
datos_limpios = normalizacion.datos
for fila in datos_limpios:
    print(fila)
