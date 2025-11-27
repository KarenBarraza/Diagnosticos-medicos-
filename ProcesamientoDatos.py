from GestionarArchivo import GestionarArchivo
from NormalizacionDatos import NormalizacionDatos

gestor = GestionarArchivo()
datos = gestor.leer_datos("dataset5_patient_diagnoses.csv")

for dato in datos:
    normalizar = NormalizacionDatos()
    dato["admission_date"] = normalizar.convertirFecha(dato["admission_date"], "%Y-%m-%d")
    dato["discharge_date"] = normalizar.convertirFecha(dato["discharge_date"], "%Y-%m-%d")

# for i in datos:
    print(datos)

