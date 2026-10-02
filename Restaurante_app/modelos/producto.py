class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @staticmethod
    def validar_texto(valor, campo):
        # Reutiliza una validacion basica para datos obligatorios.
        if not valor or not valor.strip():
            raise ValueError(f"El campo {campo} no puede estar vacio.")
        return valor.strip()

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = self.validar_texto(valor, "codigo")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = self.validar_texto(valor, "nombre")

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        valor_float = float(valor)
        if valor_float < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor_float

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        valor_int = int(valor)
        if valor_int < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = valor_int

    def _str_(self):
        return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f}"

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            data.get("codigo", ""),
            data.get("nombre", ""),
            float(data.get("precio", 0)),
            int(data.get("stock", 0))
        )
   