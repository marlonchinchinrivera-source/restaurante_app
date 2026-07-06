class Producto:
    def __init__(self, nombre: str, precio: float, disponible: bool = True):
        self.nombre = nombre
        if precio <= 0:
            raise ValueError("El precio inicial debe ser mayor a cero.")
        self.__precio = precio  # Atributo privado encapsulado
        self.disponible = disponible

    def obtener_precio(self) -> float:
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print(f"[Error]: El precio de '{self.nombre}' debe ser mayor a cero.")

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}"