from NormalizacionDatos import NormalizacionDatos as Nor
from GestionarArchivo import GestionarArchivo as ges

archivo=ges()
datos=archivo.leer_datos("dataset5_patient_diagnoses.csv")

funsion=Nor()

while True:
    print("Menu \n 1. ver lista \n 2. no dificar espacion en blanco LOSD")
    opcion=input()

    if opcion=="1":
        funsion.MostrarListado(datos)
        menu=input()
    elif opcion=="2":
        funsion.RemplasarEspaciosBacios(datos)
        menu=input()

    else:
        print("opcion no valida vuelve a intentarlo")
        menu=input()
        