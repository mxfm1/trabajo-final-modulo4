from dataclasses import dataclass

@dataclass
class Producto:
    sku:int
    nombre:str
    categoria:str
    proveedor:str
    stock:int
    valor_neto:int
    _impuesto:float = 0
    
    def impuesto(self):
        self._impuesto = self.valor_neto * 0.19
        
    def __post_init__(self):
        self.impuesto()
        
    def buscar(condicion,productos):
        for producto in productos:
            if producto.sku == condicion:
                return producto
        return None
    

