from usuario import Usuario
from carro import Carro
from parqueadero import Parqueadero
from base_datos_parqueadero import base_datos_parqueadero

#---cod principal-----
bd_parqueadero = base_datos_parqueadero()

obj_usuario_1 = Usuario(12345,"Angyeli", "administradora")
obj_carro_1 = Carro("abc123", "chevrolet", "rosa")
obj_parqueadero_1 = Parqueadero("A-01", "20/02/2026", "8:30AM", " ", "entrada")
obj_fila_1 = [obj_usuario_1, obj_carro_1, obj_parqueadero_1]

obj_usuario_2 = Usuario(67890,"Carlos","vigilante")
obj_carro_2 = Carro("xyz789","toyota","negro")
obj_parqueadero_2 = Parqueadero("B-02","20/02/2026","9:15AM"," ","entrada")
obj_fila_2 = [obj_usuario_2, obj_carro_2, obj_parqueadero_2]


obj_usuario_3 = Usuario(54321,"Mariana","administradora")
obj_carro_3 = Carro("def456","mazda","blanco")
obj_parqueadero_3 = Parqueadero("C-03","20/02/2026","10:45AM"," ","entrada")
obj_fila_3 = [obj_usuario_3, obj_carro_3, obj_parqueadero_3]

bd_parqueadero.guardar_fila(obj_fila_1)
bd_parqueadero.guardar_fila(obj_fila_2)
bd_parqueadero.guardar_fila(obj_fila_3)
pregunta_info = int(input("desea ver los registros realizados en el dia de hoy?\n1.si 2.no\n"))
if pregunta_info == 1:
    bd_parqueadero.mostrar_fila()
else:
    print("gracias por visitar nuestro parqueadero")

