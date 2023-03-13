import json
from clientes import Cliente
from productos import Producto


class Datos:
    clientes = []
    vendedores = []
    productos = []
    proveedores = []
    ventas = []

    def add_clientes(self,cliente):
        self.clientes.append(cliente)
    
    def add_producto(self,producto):
        self.productos.append(producto)
    
    def add_vendedor(self,vendedor):
        self.vendedores.append(vendedor)
        
    def del_producto(self,producto):
        self.productos.remove(producto)
    
    def del_vendedor(self,vendedor):
        self.productos.remove(vendedor)
    
    def del_cliente(self,cliente):
        self.productos.remove(cliente)
        
    def update_client(self,cliente,original):
        self.clientes[self.clientes.index(original)] = cliente
        
    def guardar_clientes(self):
        with open('clientes.json','w') as archivo:
            archivo.write(json.dumps(self.clientes,default=lambda o: o.__dict__, indent=4))
    
    def recuperar_clientes(self):
        try:
            with open('clientes.json','r') as archivo:
                self.clientes = json.loads(archivo.read(), object_hook= lambda d: Cliente(**d))
        except:
            return self.clientes
    
    def guardar_productos(self):
        with open('productos.json', 'w') as archivo:
            archivo.write(json.dumps(self.productos, default=lambda o: o.__dict__, indent=4))
            
    def recuperar_productos(self):
        try:
            with open('productos.json', 'r') as archivo:
                self.productos = json.loads(archivo.read(), object_hook=lambda d: Producto(**d))
        except:
            self.productos = []
    