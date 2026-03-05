class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        
    def get_nombre(self):
        return self.nombre
    def get_cedula(self):
        return self.cedula
    
    def mostrar_info_almacenada(self):
        mensaje = (f"{self.get_nombre()} | {self.get_cedula()}")
        return mensaje