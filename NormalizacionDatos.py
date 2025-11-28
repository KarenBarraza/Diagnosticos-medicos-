#Se importa la clase necesaria para trabajar
from GestionarArchivo import GestionarArchivo
#Se importa una libreria con el formato de fecha
from datetime import datetime , timedelta

#Se crea una clase que tendra las funciones necesarias para normalizar los datos
class NormalizacionDatos:
    def __init__(self):
        pass
#Funcion para corregir la escritura (todo creara escrito con mayusucula iniciañ y minusuculas)           
    def normalizar_texto(self, texto):
        if not texto:
            return ""
#Convierte todo a minúscula y luego la primera letra a mayúscula
        return texto.lower().capitalize()
#Limpia las filas "diaggnosis" y "diagnosis group"
    def limpiar_diagnosticos(self,datos):
        for fila in datos:
            fila["diagnosis"] = self.normalizar_texto(fila.get("diagnosis", ""))
            fila["diagnosis_group"] = self.normalizar_texto(fila.get("diagnosis_group", ""))

#Normaliza las palabras "SI" y "NO" para que queden escritas de manera correcta
    def normalizar_valor(self, valor):
        datos = valor.strip().lower()
        if datos in ("si", "SÃ­"):
            return "SI"
        elif datos in ("no", "no"):
            return "NO"
        else:
            return datos
#Inicia un contador de "id" desde 1001 hasta el ultimo valor que encuentre 
    def renumerar_ids(self, filas):
        contador = 1001
        for fila in filas:
            fila["patient_id"] = contador
            contador += 1
        return filas

#Convierte todas las fechas del archivo a un solo formato de fecha (Y/m/d)
    formatos_entrada = ["%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y"]

    def convertirFecha(self, fecha, formato_salida):
        for f in self.formatos_entrada:
            try:
                return datetime.strptime(fecha, f).strftime(formato_salida)
#Si encuentra un error retorna "0000-00-00"
            except ValueError:
                continue
        return "0000-00-00"
        
#Calcula la fecha de salida con la fecha de ingreso y los dias de estadia en el hospital
    def calcular_fecha_salida(self,datos):
        for lista in datos:
            if lista["discharge_date"]=='0000-00-00':
                if lista['length_of_stay_days']<=0:
                    lista["discharge_date"]=lista['admission_date']
                else:
                    ingresoF = datetime.strptime(lista['admission_date'],"%Y-%m-%d")
                    salidaF=ingresoF+ timedelta(days=lista['length_of_stay_days'])
                    lista["discharge_date"] = salidaF.strftime("%Y-%m-%d")

#No se utiliza
    #def procesar_datos(self):
        #for dato in self.datos:
            #dato["admission_date"] = self.normalizar.convertirFecha(dato["admission_date"], "%Y-%m-%d")
            #if dato["discharge_date"] in dato and dato["discharge_date"] == " ":
                #dias_hospitalizacion = int(dato.get("length_of_stay_days", 1) or 1)
                #dato["discharge_date"] = self.calcular_fecha_salida(dato["admission_date"], dias_hospitalizacion)

#Funcion para mostrar toda la lista
    def MostrarListado(self,datos):
        for lista in datos:
            print(lista)

#Remplaza los vacios o N/A con 0 de la columna de estadia
    def ReemplazarEspaciosVacios(self,datos):
        for lista in datos:
            if lista['length_of_stay_days'] == "":
                lista['length_of_stay_days']=0
            elif lista['length_of_stay_days'] == "NA":
                lista['length_of_stay_days']=0
            else:
                lista['length_of_stay_days']=int(lista['length_of_stay_days'])

 #Se remplazan los dias para crear logica con las dos fechas (Ingreso y salida)  
    def ModificacionDias(self,datos):
        for lista in datos:
            if isinstance(lista["admission_date"], str):
                f1 = datetime.strptime(lista["admission_date"], "%Y-%m-%d")
            else:
                f1 = lista["admission_date"]
            if isinstance(lista["discharge_date"], str):
                f2 = datetime.strptime(lista["discharge_date"], "%Y-%m-%d")
            else:
                f2 = lista["discharge_date"]
            dias=(f2-f1).days
            if dias <=0:
                dias=1
            lista['length_of_stay_days']=dias
                
#Crea el archivo y lo imprime
    def CrearArchivo(self,datos):
        gestor=GestionarArchivo()
        Nombre_colupnas=[
            'record_id','patient_id','age','gender',
            'diagnosis','diagnosis_group','admission_date',
            'discharge_date','severity','has_comorbidities',
            'length_of_stay_days','outcome']
        ruta="pacientes_diagnosticados.csv"
        gestor.escribir_csv(ruta,datos,Nombre_colupnas)


            


