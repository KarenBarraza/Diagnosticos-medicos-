from GestionarArchivo import GestionarArchivo
from datetime import datetime
from datetime import timedelta

class NormalizacionDatos:
    def _init_(self):
        pass

    formatos_entrada = ["%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y"]

    def convertirFecha(self, fecha, formato_salida):
        for f in self.formatos_entrada:
            try:
                return datetime.datetime.strptime(fecha, f).strftime(formato_salida)
            except ValueError:
                continue
        return "0000-00-00"
    

    # def calcular_fecha_salida(fecha_ingreso, dias_hospitalizacion):
    #     fecha_ingreso = datetime.datetime.strptime(fecha_ingreso, "%Y-%m-%d")
    #     fecha_salida = fecha_ingreso + datetime.timedelta(days=dias_hospitalizacion)
    #     return fecha_salida.strftime("%Y-%m-%d")

    # for dato in datos:
    #     if dato["discharge_date"] == "":
    #         dato["discharge_date"] = calcular_fecha_salida(dato["admission_date"], dato["length_of_stay_days"])

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

