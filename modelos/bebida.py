from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, volumen_ml: int, disponible: bool = True):
        super().__init__(nombre, precio, disponible)
        self.volumen_ml = volumen_ml

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base} | Tamaño: {self.volumen_ml} ml (Bebida)"