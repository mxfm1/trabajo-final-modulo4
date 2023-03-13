from dataclasses import asdict
from data_class import Datos
from presentacion import  editar_productos, encontrar_clientes, menu_principal, menu_clientes, editar_clientes,end,listar_clientes, menu_productos
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
                    
                        
            if new_option == 4:
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
            producto = editar_productos('Crear',None)
            datos.productos.append(producto)
            datos.guardar_productos()
            print('Producto guardado exitosamente. ')
        if new_option == 4:
            for producto in datos.productos:
                print(producto)
    if option == 0:
        print('exit')
        break
    # except:
    #     pass
    # break