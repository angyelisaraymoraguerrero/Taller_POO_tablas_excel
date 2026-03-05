class Carro:
    def __init__(self,placa, tipo, color):
        self.placa = placa
        self.tipo = tipo
        self.color = color
        
    def get_placa(self):
        return self.placa
    def get_tipo(self):
        return self.tipo
    def get_color(self):
        return self.color
    
    def set_placa(self, placa):
        self.placa = placa
    def set_tipo(self, tipo):
        self.tipo = tipo
    def set_color(self, color):
        self.color = color
        
    def mostrar_info(self):
        print(f"placa: {self.get_placa()}")
        print(f"tipo: {self.get_tipo()}")
        print(f"color: {self.get_color()}")
        
        