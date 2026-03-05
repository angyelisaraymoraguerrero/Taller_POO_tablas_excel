class base_datos:
    def __init__(self):
        self.lista = []
    def guardar_obj(self, obj_usuario):
        self.lista.append(obj_usuario)
        
    def mostrar_info(self):
        for fila in self.lista:
              print("----------------------------")
              mensaje = " "
              for i in fila:
                mensaje += i.mostrar_info_almacenada() + " | "
              print(mensaje)