class base_datos_parqueadero:
    def __init__(self):
        self.lista_parqueadero = []
    
    def guardar_fila(self, obj_fila):
        self.lista_parqueadero.append(obj_fila)
        
    def mostrar_fila(self):
        for fila in self.lista_parqueadero:
            print("----------------------------")
            for objeto in fila:
                objeto.mostrar_info()