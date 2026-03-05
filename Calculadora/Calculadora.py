class Calculadora:
    def __init__(self,numero_1,numero_2,tipo_operacion,resultado, fecha_uso):
        self.numero_1 = numero_1
        self.numero_2 = numero_2
        self.tipo_operacion = tipo_operacion
        self.resultado = resultado
        self.fecha_uso = fecha_uso
        
    def get_numero_1(self):
        return self.numero_1
    def get_numero_2(self):
        return self.numero_2
    def get_tipo_operacion(self):
        return self.tipo_operacion
    def get_resultado(self):
        return self.resultado
    def get_fecha_uso(self):
        return self.fecha_uso
    
    def sumar(self):
        self.resultado = self.numero_1 + self.numero_2
        return self.resultado 
    def restar(self):
        self.resultado = self.numero_1 - self.numero_2
        return self.resultado 
    def multiplicar(self):
        self.resultado = self.numero_1 * self.numero_2
        return self.resultado 
    def dividir(self):
        self.resultado = self.numero_1 / self.numero_2
        return self.resultado 
    
    def mostrar_info_almacenada(self):
        mensaje = (f"{self.get_numero_1()} | {self.get_numero_2()} | {self.get_tipo_operacion()} | {self.get_resultado()} | {self.get_fecha_uso()}")
        return mensaje
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        