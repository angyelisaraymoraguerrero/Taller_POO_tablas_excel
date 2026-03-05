from base_datos import base_datos
from Calculadora import Calculadora
from Usuario import Usuario

# Codigo principal

bd_calculadora = base_datos()

obj_calculadora_1 = Calculadora(10,2,"  division ","" ,"  01-02-2025") 
obj_usuario_1 = Usuario("angyeli","1234")
obj_calculadora_1.dividir()

obj_completo_1 = [obj_usuario_1,obj_calculadora_1]
bd_calculadora.guardar_obj(obj_completo_1)


obj_calculadora_2 = Calculadora(7,7,"multiplicacion","" ,"  01-02-2025") 
obj_usuario_2 = Usuario(" Saray ","54321")
obj_calculadora_2.multiplicar()
obj_completo_2 = [obj_calculadora_2, obj_usuario_2 ]

obj_completo_2 = (obj_usuario_2,obj_calculadora_2)
bd_calculadora.guardar_obj(obj_completo_2)

print("nombre | cedula | n1 | n2 | operacion | resultado | fecha de uso")
bd_calculadora.mostrar_info()

