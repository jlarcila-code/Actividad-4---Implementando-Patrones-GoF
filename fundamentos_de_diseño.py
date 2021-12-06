from abc import ABC, abstractmethod

class Fundamentos_de_Diseño(ABC):
    def __init__(self) -> None:
        self._descripcion = "Cualquier actividad"

    def set_descripcion(self, valor: str) -> None:
        self._descripcion = valor

    def get_descripcion(self) -> str:
        return self._descripcion

    @abstractmethod
    def calcular_nota(self) -> float:
        raise NotImplementedError

class Actividad_01(Fundamentos_de_Diseño):
    def __init__(self) -> None:
        self._descripcion = "Actividad_01"

    def calcular_nota(self) -> float:
        return 4.0

class Actividad_02(Fundamentos_de_Diseño):
    def __init__(self) -> None:
        self._descripcion = "Actividad_02"

    def calcular_nota(self) -> float:
        return 4.5

class Actividad_03(Fundamentos_de_Diseño):
    def __init__(self) -> None:
        self._descripcion = "Actividad_03"

    def calcular_nota(self) -> float:
        return 3.5

