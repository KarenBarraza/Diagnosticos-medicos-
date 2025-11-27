from GestionarArchivo import GestionarArchivo

class NormalizacionDatos:
    def __init__(self, columna,inicio=1001):
        self.columna = columna
        self.inicio = inicio

    def normalizar_valor(self, valor):
        datos = valor.strip().lower()
        if datos in ("si", "SÃ­"):
            return "SI"
        elif datos in ("no", "no"):
            return "NO"
        else:
            return datos

    def renumerar_ids(self, filas):
        contador = self.inicio
        for fila in filas:
            fila["patient_id"] = contador
            contador += 1
        return filas