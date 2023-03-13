import datetime
from persona import Persona
from dataclasses import dataclass

@dataclass
class Vendedor(Persona):
    seccion:str
    _comision:float

    @classmethod
    def vender(self,producto,cliente):
        cantidad = int(input('Cuantas unidades del producto quieres comprar:  '))
        while cantidad > producto.stock:
            print('La cantidad supera al stock del producto. Porfavor ingresa una cantidad menor al stock. ')
            cantidad = int(input('Cuantas unidades vas a llevar: '))
        producto.stock -= cantidad
        print(f'Se compraron {cantidad} unidades de {producto.nombre}. El stock actual del producto es {producto.stock}')

        valor_neto_total = (producto.valor_neto * cantidad)
        impuesto = valor_neto_total * 0.19
        comision = (valor_neto_total + impuesto) * 0.005
        valor_final = valor_neto_total + impuesto + comision
        cliente._saldo -= valor_final
        print(f'Se decontó {valor_final} del saldo del cliente. El saldo actual del cliente es: {cliente._saldo}')
        date = datetime.datetime.now()
        
        detalles_venta = {}
        detalles_venta['PRODUCTO'] = producto.nombre
        detalles_venta['CANTIDAD'] =  cantidad
        detalles_venta['VALOR NETO'] = valor_neto_total
        detalles_venta['IMPUESTOS'] = impuesto
        detalles_venta['COMISION VENDEDOR'] = comision
        detalles_venta['FECHA'] = date.strftime("%d %B %Y")
        detalles_venta['TOTAL'] = valor_final
        
        return detalles_venta
        
        
        
        
        
        
        

