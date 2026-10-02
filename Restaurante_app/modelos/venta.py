class Venta:
    def __init__(self, identificador, usuario_id, producto_codigo, fecha):
        self.identificador = identificador
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.fecha = fecha

    @staticmethod
    def validar_texto(valor, campo):
        if not valor or not str(valor).strip():
            raise ValueError(f"El campo {campo} no puede estar vacío.")
        return str(valor).strip()

    @property
    def identificador(self):
        return self._identificador

    @identificador.setter
    def identificador(self, valor):
        self._identificador = self.validar_texto(valor, "identificador")

    @property
    def usuario_id(self):
        return self._usuario_id

    @usuario_id.setter
    def usuario_id(self, valor):
        self._usuario_id = self.validar_texto(valor, "usuario_id")

    @property
    def producto_codigo(self):
        return self._producto_codigo

    @producto_codigo.setter
    def producto_codigo(self, valor):
        self._producto_codigo = self.validar_texto(valor, "producto_codigo")

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = self.validar_texto(valor, "fecha")

    def to_dict(self):
        return {
            "identificador": self.identificador,
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "fecha": self.fecha,
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            identificador=datos.get("identificador"),
            usuario_id=datos.get("usuario_id"),
            producto_codigo=datos.get("producto_codigo"),
            fecha=datos.get("fecha"),
        )