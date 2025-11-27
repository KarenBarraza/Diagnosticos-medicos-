from GestionarArchivo import GestionarArchivo
from NormalizacionDatos import NormalizacionDatos

gestor = GestionarArchivo()
datos = gestor.leer_datos("dataset5_patient_diagnoses.csv")

normalizar = NormalizacionDatos()
normalizar.limpiar_diagnosticos(datos)
normalizar.RemplasarEspaciosBacios(datos)

for dato in datos:
    dato["admission_date"] = normalizar.convertirFecha(dato["admission_date"], "%Y-%m-%d")
    dato["discharge_date"] = normalizar.convertirFecha(dato["discharge_date"], "%Y-%m-%d")

while True:
    print("Menu \n 1. ver lista \n 2. no dificar espacion en blanco LOSD")
    opcion=input()

    if opcion=="1":
        normalizar.MostrarListado(datos)
        menu=input()
    elif opcion=="2":
        
        menu=input()

    else:
        print("opcion no valida vuelve a intentarlo")
        menu=input()
        
