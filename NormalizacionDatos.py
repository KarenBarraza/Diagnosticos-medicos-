from GestionarArchivo import GestionarArchivo

class NormalizacionDatos:
    def __init__(self, columna,inicio=1001):
        self.columna = columna
        self.inicio = inicio

    def normalizar_valor(self, valor):
        valor = valor.strip().lower()
        if valor in ("si", "SÃ­"):
            return "SI"
        elif valor in ("no", "no"):
            return "NO"
        else:
            return valor

    def renumerar_ids(self, filas):
        contador = self.inicio
        for fila in filas:
            fila["patient_id"] = contador
            contador += 1
        return filas