from persona import Persona
from dataclasses import dataclass

@dataclass
class Vendedor(Persona):
    seccion:str
    _comision:float


        

