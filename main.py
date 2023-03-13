from productos import Producto
from data_class import Datos
from clientes import Cliente
from vendedores import Vendedor

from presentacion import listar_clientes,encontrar_clientes

datos = Datos()

datos.add_clientes(Cliente(rut='1-9',nombre='Juan',apellido='Espindola'))
datos.add_clientes(Cliente(rut='1-9',nombre='Luis',apellido='Gallego'))


datos.add_vendedor(Vendedor('1-9', 'Mario', 'Perez'))
datos.add_vendedor(Vendedor('2-9', 'Mauricio', 'Gonzalez'))
datos.add_vendedor(Vendedor('3-9', 'Josefina', 'Gonzalez'))
datos.add_vendedor(Vendedor('4-9', 'Antonia', 'Perez'))
datos.add_vendedor(Vendedor('5-9', 'Paz', 'Gonzalez'))

datos.guardar_clientes()
datos.add_producto(Producto(201,'tarjeta grafica','gaming','PC Factory',300,200000))
for producto in datos.productos:
    print(producto)
listar_clientes(datos.clientes)
