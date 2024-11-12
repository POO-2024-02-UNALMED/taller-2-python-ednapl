class Asiento:
    # Constructor de la clase Asiento
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    # Método para cambiar el color del asiento
    def cambiarColor(self, nuevo_color):
        # Cambia el color solo si es uno de los colores permitidos
        if nuevo_color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color = nuevo_color

class Motor:
    # Constructor de la clase Motor
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    # Método para cambiar el registro del motor
    def cambiarRegistro(self, nuevo_registro):
        self.registro = nuevo_registro

    # Método para asignar el tipo de motor, solo permite "electrico" o "gasolina"
    def asignarTipo(self, nuevo_tipo):
        if nuevo_tipo in ["electrico", "gasolina"]:
            self.tipo = nuevo_tipo

class Auto:
    # Atributo de clase para llevar el conteo de los autos creados
    cantidadCreados = 0

    # Constructor de la clase Auto
    def __init__(self, modelo, precio, marca, motor, registro, asientos):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.asientos = asientos  # Lista de objetos Asiento
        Auto.cantidadCreados += 1

    # Método para contar la cantidad de asientos válidos en el auto
    def cantidadAsientos(self):
        # Solo cuenta los elementos que son instancias de la clase Asiento
        return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))

    # Método para verificar la integridad del auto
    def verificarIntegridad(self):
        # Revisa si el registro del auto, el motor y cada asiento es el mismo
        if self.registro == self.motor.registro and all(asiento.registro == self.registro for asiento in self.asientos):
            return "Auto original"
        else:
            return "Las piezas no son originales"
