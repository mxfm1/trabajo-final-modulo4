from random import randint
from persona import Persona


class Cliente(Persona):
    _saldo : int
    
    def __init__(self,**kwargs):
        # super().__init__(**kwargs)
        if 'rut' in kwargs:
            self.rut = kwargs['rut']
        if 'nombre' in kwargs:
            self.nombre = kwargs['nombre']
        if 'apellido' in kwargs:
            self.apellido = kwargs['apellido']
        self._saldo = randint(10000,30000)
        

    def buscar(self,rut,clientes):
        for cliente in clientes:
            if cliente.rut == rut:
                return cliente
        return None
