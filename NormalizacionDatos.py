from GestionarArchivo import GestionarArchivo
from datetime import datetime

class NormalizacionDatos:
    def __init__(self):
        pass

    formatos_entrada = ["%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y"]

    def convertirFecha(self, fecha, formato_salida):
        for f in self.formatos_entrada:
            try:
                return datetime.strptime(fecha, f).strftime(formato_salida)
            except ValueError:
                continue
            return "0000-00-00"
        

    def calcular_fecha_salida(self, fecha_ingreso, dias_hospitalizacion):
        fecha_ingreso = datetime.datetime.strptime(fecha_ingreso, "%Y-%m-%d")
        fecha_salida = fecha_ingreso + datetime.timedelta(days=dias_hospitalizacion)
        return fecha_salida.strftime("%Y-%m-%d")


    def procesar_datos(self):
        for dato in self.datos:
            dato["admission_date"] = self.normalizar.convertirFecha(dato["admission_date"], "%Y-%m-%d")
            if dato["discharge_date"] in dato and dato["discharge_date"] == " ":
                dias_hospitalizacion = int(dato.get("length_of_stay_days", 1) or 1)
                dato["discharge_date"] = self.calcular_fecha_salida(dato["admission_date"], dias_hospitalizacion)


    def MostrarListado(self,datos):
        for lista in datos:
            print(lista)


    def ReemplazarEspaciosVacios(self,datos):
        for lista in datos:
            if lista['length_of_stay_days'] == "":
                lista['length_of_stay_days']=0
            elif lista['length_of_stay_days'] == "NA":
                lista['length_of_stay_days']=0
            else:
                lista['length_of_stay_days']=int(lista['length_of_stay_days'])

