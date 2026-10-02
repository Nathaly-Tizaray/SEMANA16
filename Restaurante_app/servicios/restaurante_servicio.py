from datetime import datetime
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class RestauranteServicio:

  def __init__(self, archivo_servicio):
    self.archivo_servicio = archivo_servicio
    self.usuarios = []
    self.productos = []
    self.ventas = []
    self.cargar_datos()

  def cargar_datos(self):
    usuarios_json = self.archivo_servicio.leer_json("usuarios.json")
    if usuarios_json:
      self.usuarios = [Usuario.from_dict(datos) for datos in usuarios_json]
    else:
      self.usuarios = []

    productos_json = self.archivo_servicio.leer_json("productos.json")
    if productos_json:
      self.productos = [Producto.from_dict(datos) for datos in productos_json]
    else:
      self.productos = []

    ventas_json = self.archivo_servicio.leer_json("ventas.json")
    if ventas_json:
      self.ventas = [Venta.from_dict(datos) for datos in ventas_json]
    else:
      self.ventas = []

  def validar_acceso(self, usuario, contrasena):
    for usuario_registrado in self.usuarios:
      if (
          usuario_registrado.usuario == usuario
          and usuario_registrado.contrasena == contrasena
      ):
        return usuario_registrado
    return None

  def cantidad_usuarios(self):
    return len(self.usuarios)

  def cantidad_productos(self):
    return len(self.productos)

  def listar_usuarios(self):
    return self.usuarios

  def guardar_usuarios(self):
    datos = [usuario.to_dict() for usuario in self.usuarios]
    self.archivo_servicio.escribir_json("usuarios.json", datos)

  def buscar_usuario_por_identificador(self, identificador):
    for usuario in self.usuarios:
      if usuario.identificador == identificador:
        return usuario
    return None

  def buscar_usuario_por_nombre_usuario(self, nombre_usuario):
    for usuario in self.usuarios:
      if usuario.usuario == nombre_usuario:
        return usuario
    return None  # Corregido: fuera del bucle for

  # ==================================
  # CRUD DE USUARIOS Y PERSISTENCIA
  # ==================================
  def registrar_usuario(self, identificador, nombre, usuario, contrasena, rol):
    if self.buscar_usuario_por_identificador(identificador) is not None:
      raise ValueError("Ya existe un usuario con este identificador.")

    if self.buscar_usuario_por_nombre_usuario(usuario) is not None:
      raise ValueError("El nombre de usuario ya está registrado.")

    nuevo_usuario = Usuario(identificador, nombre, usuario, contrasena, rol)
    self.usuarios.append(nuevo_usuario)
    self.guardar_usuarios()

  def listar_productos(self):
    return self.productos

  # ==================================
  # CRUD DE PRODUCTOS Y PERSISTENCIA
  # ==================================
  def guardar_productos(self):
    datos = [producto.to_dict() for producto in self.productos]
    self.archivo_servicio.escribir_json("productos.json", datos)

  def buscar_producto_por_codigo(self, codigo):
    for producto in self.productos:
      if producto.codigo == codigo:
        return producto
    return None

  def registrar_producto(self, codigo, nombre, precio, stock):
    if not codigo or not nombre or not precio or not stock:
      raise ValueError("Todos los campos del producto son obligatorios.")

    try:
      precio_val = float(precio)
      stock_val = int(stock)
    except ValueError:
      raise ValueError(
          "El precio debe ser un número decimal y el stock un número entero."
      )

    if precio_val <= 0 or stock_val < 0:
      raise ValueError(
          "El precio debe ser mayor a 0 y el stock no puede ser negativo."
      )

    if self.buscar_producto_por_codigo(codigo) is not None:
      raise ValueError("Ya existe un producto registrado con este código.")

    nuevo_producto = Producto(codigo, nombre, precio_val, stock_val)
    self.productos.append(nuevo_producto)
    self.guardar_productos()

  def actualizar_producto(self, codigo, nombre, precio, stock):
    if not codigo or not nombre or not precio or not stock:
      raise ValueError("Todos los campos son obligatorios para actualizar.")

    producto = self.buscar_producto_por_codigo(codigo)
    if producto is None:
      raise ValueError("No se encontró el producto a actualizar.")

    try:
      precio_val = float(precio)
      stock_val = int(stock)
    except ValueError:
      raise ValueError(
          "El precio debe ser un número decimal y el stock un número entero."
      )

    producto.nombre = nombre
    producto.precio = precio_val
    producto.stock = stock_val
    self.guardar_productos()

  def eliminar_producto(self, codigo):
    if not codigo:
      raise ValueError("Debe ingresar el código del producto a eliminar.")

    producto = self.buscar_producto_por_codigo(codigo)
    if producto is None:
      raise ValueError("No existe un producto con ese código.")

    self.productos.remove(producto)
    self.guardar_productos()

  # ==================================
  # GESTIÓN DE VENTAS Y PERSISTENCIA
  # ==================================
  def listar_ventas(self):
    return self.ventas

  def guardar_ventas(self):
    datos = [venta.to_dict() for venta in self.ventas]
    self.archivo_servicio.escribir_json("ventas.json", datos)

  def registrar_venta(self, usuario_id, producto_codigo):
    nuevo_id = str(len(self.ventas) + 1)
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nueva_venta = Venta(
        identificador=nuevo_id,
        usuario_id=usuario_id,
        producto_codigo=producto_codigo,
        fecha=fecha_actual,
    )

    self.ventas.append(nueva_venta)
    self.guardar_ventas()
    return nueva_venta