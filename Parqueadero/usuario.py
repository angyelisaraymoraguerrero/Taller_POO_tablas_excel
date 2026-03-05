class Usuario:
    def __init__(self, cedula, nombre, tipo):
        self.cedula = cedula
        self.nombre = nombre
        self.tipo = tipo
        
    def get_cedula(self):
        return self.cedula
    def get_nombre(self):
        return self.nombre
    def get_tipo(self):
        return self.tipo
    
    def set_cedula(self, cedula):
         self.cedula = cedula
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_tipo(self, tipo):
        self.tipo = tipo
        
    def mostrar_info(self):
        print (f"nombre: {self.get_nombre()}")
        print (f"cedula: {self.get_cedula()}")
        print (f"tipo de usuario {self.get_tipo()}")