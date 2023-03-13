from dataclasses import asdict
import os
from clientes import Cliente
from productos import Producto
from vendedores import Vendedor
from data_class import Datos

def end():
    print('')
    val = int(input('Presione 0 para continuar...'))
    return val

def menu_principal():
    # os.system("cls")
    print("MENÚ PRINCIPAL - SISTEMA DE VENTAS")
    print("1. Menú Clientes")
    print("2. Menú Vendedores")
    print("3. Menú Productos")
    print("4. Registrar venta")
    print("5. Listar Ventas")
    print("0. Salir")

def menu_clientes():
    os.system("cls")
    print("-----> MENÚ CLIENTES <-----")
    print("1. Agregar cliente")
    print("2. Eliminar cliente")
    print("3. Modificar cliente")
    print("4. Listar clientes")
    print("0. Volver")

def menu_vendedores():
    os.system("cls")
    print("-----> MENÚ VENDEDORES <-----")
    print("1. Agregar vendedor")
    print("2. Eliminar vendedor")
    print("3. Modificar vendedor")
    print("4. Listar vendedor")
    print("0. Volver")
    
def menu_productos():
    os.system("cls")
    print("-----> MENÚ PRODUCTOS <-----")
    print("1. Agregar Productos")
    print("2. Eliminar Productos")
    print("3. Modificar Productos")
    print("4. Listar Productos")
    print("0. Volver")
# def listar_clientes_del(index):
#     id = len()

def listar_clientes(clientes):
    print('=============================================')
    print('----------Listado de Clientes----------')
    print('=============================================')
    for cliente in clientes:
        print(f'Cliente: {cliente.nombre} {cliente.apellido}  RUT: {cliente.rut}')
        
def listar_productos(productos):
    print('=============================================')
    print('----------Listado de Productos----------')
    print('=============================================')
    for producto in productos:
        print(producto)

def editar_clientes(accion:str,cliente:Cliente) -> Cliente:
    os.system("cls")
    print("=============================================")
    print("----------> ",accion.upper(), "CLIENTE <----------")
    print("=============================================")
    registro = { "rut": "", "nombre": "", "apellido": "" }
    if cliente is not None:
        registro['rut'] = cliente.rut
        registro['nombre'] = cliente.nombre
        registro['apellido'] = cliente.apellido
        
    rut = input("RUT [" + registro['rut'] +  "]:")
    nombre = input("Nombre [" + registro["nombre"] + "]: ")
    apellido = input("Apellido [" + registro["apellido"] + "]: ")

    if rut != "":
        registro["rut"] = rut
    if nombre != "":
        registro["nombre"] = nombre
    if apellido != "":
        registro["apellido"] = apellido
    return Cliente(rut=registro["rut"], nombre=registro["nombre"], apellido=registro["apellido"])
    
def editar_productos(accion:str, producto: Producto) -> Producto:
    os.system('cls')
    print('=============================================')
    print('---------Lista Productos---------')
    print('=============================================')
    registro = {"sku":"","nombre":"","categoria":"","proveedor":"","stock":"","valor_neto":""}
    if producto is not None:
        registro['sku'] = producto.sku
        registro['nombre'] = producto.nombre
        registro['categoria'] = producto.categoria
        registro['proveedor'] = producto.proveedor
        registro['stock'] = producto.stock
        registro['valor_neto'] = producto.valor_neto
            
    sku = input('Ingresa el sku del producto: ')
    nombre = input('Ingresa el nombre del producto: ')
    categoria = input('Ingresa la categoria del producto')
    proveedor = input('Ingresa el proveedor del producto: ')
    stock = input('Ingresa el stock del producto: ')
    valor_neto = input('Ingresa el stock del producto: ')
    
    if sku != '':
        registro['sku'] = sku
    if nombre != '':
        registro['nombre'] = nombre
    if categoria != '':
        registro['categoria'] = categoria
    if proveedor != '':
        registro['proveedor'] = proveedor
    if stock != '':
        registro['stock'] = stock
    if valor_neto != '':
        registro['valor_neto'] = valor_neto
    return Producto(sku=registro["sku"],nombre=registro["nombre"],categoria=registro["categoria"],proveedor=registro["proveedor"],stock=registro['stock'],valor_neto=registro['valor_neto'])

def crear_producto():
    print('=============================================')
    print('Agregar Producto')
    print('=============================================')
    
    sku = int(input('Ingresa el SKU del producto: '))
    nombre = str(input('Ingresa el nombre del producto: '))
    categoria = str(input('Ingresa la categoria del producto: '))
    proveedor = str(input('Ingresa el proveedor del producto: '))
    stock = int(input('Ingresa el stock del producto: '))
    valor_neto = int(input('Ingresa el valor neto del producto: '))
    
    if sku != '':
        p_sku = sku
    if nombre != '':
        p_nombre = nombre
    if categoria != '':
        p_categoria = categoria
    if proveedor != '':
        p_proveedor = proveedor
    if stock != '':
        p_stock = stock
    if valor_neto != '':
        p_valor_neto = valor_neto
    return Producto(p_sku,p_nombre,p_categoria,p_proveedor,p_stock,p_valor_neto)


def encontrar_clientes(clientes):
    print('=============================================')
    print('Buscar Cliente')
    print('=============================================')
    condicion = input('Ingrese el rut del cliente (vacio para terminar)')
    if condicion == '':
        return None
    else:
        cliente = Cliente().buscar(condicion,clientes)
        if cliente == None:
            print('Cliente no encontrado. Porfavor inténtelo nuevamente')
        else:
            return cliente
        
def encontrar_producto(productos):
    condicion = int(input('Ingresa el SKU del producto que quieras comprar: '))
    if condicion is None:
        return None
    else:
        producto = Producto.buscar(condicion,productos)
        if producto == None:
            print('Producto no encontrado. Porfavor inténtelo nuevamente')
        else:
            print(f'El producto seleccionado es: {producto.nombre}')
            return producto
        
def vender_producto(producto,cliente):
    detalles =  Vendedor.vender(producto,cliente)
    Datos.ventas.append(detalles)
    
