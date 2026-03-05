class Parqueadero:
    def __init__(self, puesto_carro, fecha_entrada, hora_entrada, hora_salida, estado):
        self.puesto_carro = puesto_carro
        self.fecha_entrada = fecha_entrada
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.estado = estado
        
    def get_puesto_carro(self):
        return self.puesto_carro
    def get_fecha_entrada(self):
        return self.fecha_entrada
    def get_hora_entrada(self):
        return self.hora_entrada
    def get_hora_salida(self):
        return self.hora_salida
    def get_estado(self):
        return self.estado
    
    def set_puesto_carro(self, puesto_carro):
        self.puesto_carro= puesto_carro
    def set_fecha_entrada(self,fecha_entrada):
        self.fecha_entrada = fecha_entrada
    def set_hora_entrada(self, hora_entrada):
        self.hora_entrada = hora_entrada
    def set_hora_salida(self, hora_salida):
        self.hora_salida = hora_salida
    def set_estado(self, estado):
        self.estado = estado
        
    def mostrar_info(self):
        print(f"puesto carro: {self.get_puesto_carro()}")
        print(f"fecha de entrada: {self.get_fecha_entrada()}")
        print(f"hora de salida: {self.get_hora_entrada()}")
        print(f"hora de salida: {self.get_hora_salida()}")
    