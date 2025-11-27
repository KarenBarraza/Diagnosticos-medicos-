from GestionarArchivo import GestionarArchivo
import datetime

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



   

    