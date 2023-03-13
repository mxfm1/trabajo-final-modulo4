from dataclasses import asdict
from data_class import Datos
from vendedores import Vendedor
from presentacion import  crear_producto, editar_productos, encontrar_clientes, encontrar_producto, listar_productos, menu_principal, menu_clientes, editar_clientes,end,listar_clientes, menu_productos, vender_producto
datos = Datos()

while True:
    menu_principal()
    # try:
    option = int(input('Ingresa una opción: '))
    if option == 1:
        menu_clientes()
        new_option = int(input('Que opción deseas: '))
        while new_option > 0 and new_option <= 4:
            if new_option == 1:
                cliente = editar_clientes('Agregar',None)
                datos.add_clientes(cliente)
                datos.guardar_clientes()
                print('Cliente guardado exitosamente')
                break
                # new_option = end()
            if new_option == 2:
                if datos.clientes == []:
                    print('No existen clientes registrados en la aplicación. ')
                    op = int(input('Desea recuperar los usuarios desde la base de datos o crear clientes nuevos? (1/2)'))
                    if op == 1:
                        datos.recuperar_clientes()
                        print('Usuarios recuperados exitosamente. ')
                        break
                    elif op == 2:
                        cliente = editar_clientes('Agregar',None)
                        datos.add_clientes(cliente)
                        datos.guardar_clientes()
                        print('Cliente guardado exitosamente')
                        break
                else:
                    for cliente in datos.clientes:
                        print(f'RUT: {cliente.rut} NOMBRE: {cliente.nombre} APELLIDO: {cliente.apellido}')
                
                    client = encontrar_clientes(datos.clientes)
                    if client is not None:
                        print(f'Cliente seleccionado: RUT: {client.rut} NOMBRE: {client.nombre} APELLIDO: {cliente.apellido}')
                        datos.del_cliente(client)
                        datos.guardar_clientes()
                        print('Cliente eliminado exitosamente. ')
                    break
                
            if new_option == 3:
                print('----------Modificar Cliente---------')
                for cliente in datos.clientes:
                    print(f'RUT: {cliente.rut} NOMBRE: {cliente.nombre} APELLIDO: {cliente.apellido}')
                client = encontrar_clientes(datos.clientes)
                if client is not None:
                    original_client = client
                    cliente = editar_clientes('Editar',original_client)
                    datos.update_client(cliente,original_client)
                    datos.guardar_clientes()
                    print('Cliente actualizado correctamente')
                    break
                        
            if new_option == 4:
                menu_clientes()
                listar_clientes(datos.clientes)
                break
        if new_option == 0:
            print('exit')
    if option == 2:
        print('menu vendedores')
    
    if option == 3:
        menu_productos()
        new_option = int(input('Ingrese la opción: '))
        if new_option == 1:
            producto = crear_producto()
            datos.add_producto(producto)
            datos.guardar_productos()
            print('Producto guardado exitosamente. ')
        if new_option == 4:
            datos.recuperar_productos()
            listar_productos(datos.productos)
    if option == 4:
        listar_clientes(datos.clientes)
        cliente = encontrar_clientes(datos.clientes)
        listar_productos(datos.productos)
        producto = encontrar_producto(datos.productos)
        vender_producto(producto,cliente)
    if option == 0:
        print('exit')
        break
    # except:
    #     pass
    # break