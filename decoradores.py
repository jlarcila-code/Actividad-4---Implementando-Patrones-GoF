from abc import abstractmethod
from fundamentos_de_diseño import Fundamentos_de_Diseño

class Extra(Fundamentos_de_Diseño):
    @abstractmethod
    def get_descripcion(Self) -> str:
        raise NotImplementedError

    @abstractmethod
    def calcular_nota(self) -> float:
        raise NotImplementedError
    
class Participacion_en_Clase(Extra):
    def __init__(self, fundamentos_de_diseño: Fundamentos_de_Diseño) -> None:
        self._fundamentos_de_diseño = fundamentos_de_diseño

    def get_descripcion(self) -> str:
        return f"{self._fundamentos_de_diseño.get_descripcion()}, Participación en clase"

    def calcular_nota(self) -> float:
        return self._fundamentos_de_diseño.calcular_nota()+ .5

class Trabajo_Grupal(Extra):
    def __init__(self, fundamentos_de_diseño: Fundamentos_de_Diseño) -> None:
        self._fundamentos_de_diseño = fundamentos_de_diseño

    def get_descripcion(self) -> str:
        return f"{self._fundamentos_de_diseño.get_descripcion()}, Trabajo en Grupo"

    def calcular_nota(self) -> float:
        return self._fundamentos_de_diseño.calcular_nota()+ .5



        
    