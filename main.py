from fundamentos_de_diseño import Actividad_01, Actividad_02, Actividad_03
from fundamentos_de_diseño import Fundamentos_de_Diseño
from decoradores import Participacion_en_Clase

def ver_detalle(fundamentos_de_diseño: Fundamentos_de_Diseño) -> None:
    print(f"{fundamentos_de_diseño.get_descripcion()} nota {fundamentos_de_diseño.calcular_nota()}")

if __name__ == "__main__":
    actividad01 = Actividad_01()
    actividad01 = Participacion_en_Clase(actividad01)
    ver_detalle(actividad01)


