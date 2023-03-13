from dataclasses import dataclass

class Proveedor:
    rut:str
    nombre_legal:str
    razon_social:str
    pais:str
    distincion:bool = True