#importar clases claves
from GestionarArchivo import GestionarArchivo
from NormalizacionDatos import NormalizacionDatos

#Se instancia el gestor de archivos
gestor = GestionarArchivo()
#Leer los datos desde el csv
datos = gestor.leer_datos("dataset5_patient_diagnoses.csv")

#Instancia NormalizacionDatos()
normalizar = NormalizacionDatos()
#Llama las funciones a usar
normalizar.renumerar_ids(datos)
normalizar.limpiar_diagnosticos(datos)
normalizar.ReemplazarEspaciosVacios(datos)

#normalizar fechas una por una
for dato in datos:
    dato["admission_date"] = normalizar.convertirFecha(dato["admission_date"], "%Y-%m-%d")
    dato["discharge_date"] = normalizar.convertirFecha(dato["discharge_date"], "%Y-%m-%d")
normalizar.calcular_fecha_salida(datos)
normalizar.ModificacionDias(datos)
#Menu interactivo
while True:
    print("Menu \n 1. ver lista \n 2. escribir csv")
    opcion=input()

    if opcion=="1":
        normalizar.MostrarListado(datos)
        menu=input()
    elif opcion=="2":
        normalizar.CrearArchivo(datos)
        menu=input()

    else:
        print("opcion no valida vuelve a intentarlo")
        menu=input()