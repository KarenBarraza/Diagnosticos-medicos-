from GestionarArchivo import GestionarArchivo as ges
from datetime import datetime
from datetime import timedelta

class NormalizacionDatos:
    def __init__(self):
        pass
    
    def MostrarListado(self,datos):
        for lista in datos:
            print(lista)

    def RemplasarEspaciosBacios(self,datos):
        for lista in datos:
            if lista['length_of_stay_days'] == "":
                lista['length_of_stay_days']=0
            elif lista['length_of_stay_days'] == "NA":
                lista['length_of_stay_days']=0
            else:
                lista['length_of_stay_days']=int(lista['length_of_stay_days'])

