# Restaurante App
 
## Tema
 
Semana 16: manejo de eventos aplicado a la gestión de usuarios en una aplicación de restaurante con Tkinter.
 
## Autor
 
**Nathaly Lisbeth Tinizaray Abad**
 
Carrera: Tecnologías de la Información
 
Asignatura: Programación Orientada a Objetos
 
---
 
## Objetivo
 
Evolucionar el proyecto de la Semana 15 sin reconstruirlo desde cero. La aplicación conserva el login, la arquitectura por capas, la persistencia JSON, el CRUD de productos, el registro de ventas, el menú lateral y la identidad visual.
 
En esta semana se incorpora el manejo de eventos en Tkinter aplicado a la gestión de usuarios, utilizando Treeview, Combobox, bind() y callbacks.
 
---
 
## Continuidad desde Semana 15
 
La interfaz mantiene los mismos colores, estilos, iconos, menú lateral, barra de estado y organización general.
 
La sección **Ventas** permanece como ejemplo de uso de `command=` y callbacks.
 
La sección **Usuarios** se amplía para incorporar el manejo de eventos estudiado durante la Semana 16.
 
---
 
## Nueva funcionalidad de Semana 16
 
La gestión de usuarios permite:
 
- Registrar usuarios.
- Consultar usuarios.
- Visualizar usuarios en un Treeview.
- Trabajar con roles básicos.
- Persistir información en usuarios.json.
 
### Roles disponibles
 
- Administrador
- Empleado
- Cliente
 
La cuenta administrativa existente se mantiene como responsable de la gestión del sistema.
 
### Flujo educativo
 
Interacción del usuario → evento → bind() → callback(event) → servicio → JSON → interfaz actualizada
 
---
 
## Eventos implementados
 
La aplicación permite diferenciar entre botones con `command=` y eventos asociados mediante `bind()`.
 
### Botones con command=
 
- Registrar
- Actualizar
- Eliminar
- Limpiar
- Registrar venta
 
### Eventos con bind()
 
- `<<TreeviewSelect>>`
- `<<ComboboxSelected>>`
- `<Return>`
- `<Escape>`
 
### Flujo del Treeview
 
Treeview → identificador → buscar_usuario_por_identificador() → objeto Usuario → formulario
 
---
 
## Estructura del Proyecto
 
```text
restaurante_app/
├── assets/
│ ├── icons/
│ └── logo/
├── datos/
│ ├── productos.json
│ ├── usuarios.json
│ └── ventas.json
├── modelos/
│ ├── producto.py
│ ├── usuario.py
│ └── venta.py
├── servicios/
│ ├── archivo_servicio.py
│ └── restaurante_servicio.py
├── ui/
│ ├── login_view.py
│ └── main_view.py
└── main.py
```
 
---
 
## Capas del Proyecto
 
### modelos/
 
Define las clases:
 
- Usuario
- Producto
- Venta
 
La clase Usuario incorpora el atributo **rol** junto con validaciones básicas.
 
### servicios/
 
Contiene la lógica de negocio del sistema.
 
`RestauranteServicio` administra:
 
- Usuarios
- Productos
- Ventas
- Persistencia JSON
 
### datos/
 
Almacena la información persistente del sistema mediante archivos JSON.
 
### ui/
 
Contiene las interfaces gráficas desarrolladas con Tkinter.
 
### assets/
 
Contiene logotipos e iconos utilizados por la aplicación.
 
---
 
## Pantallas Principales
 
### LoginView
 
Pantalla de inicio de sesión.
 
### Inicio
 
Panel principal con información general del restaurante.
 
### Usuarios
 
Pantalla para consultar y administrar usuarios.
 
### Productos
 
Pantalla de gestión de productos mediante CRUD.
 
### Ventas
 
Pantalla para registrar y consultar ventas realizadas.
 
---
 
## Componentes Tkinter Utilizados
 
- Label
- Entry
- ttk.Combobox
- ttk.Button
- ttk.Treeview
- ttk.Scrollbar
- Frame
- LabelFrame
- messagebox
 
---
 
## Persistencia
 
La información es almacenada mediante archivos JSON.
 
### usuarios.json
 
Contiene:
 
- Identificador
- Nombre
- Usuario
- Contraseña
- Rol
 
### productos.json
 
Contiene:
 
- Código
- Nombre
- Precio
- Stock
 
### ventas.json
 
Contiene:
 
- Identificador
- Usuario
- Producto
- Fecha
 
Los datos se cargan automáticamente al iniciar la aplicación y se actualizan después de cada operación de registro, actualización o eliminación.
 
---
 
## Control de Acceso
 
La aplicación utiliza el objeto `usuario_actual` recibido por MainView.
 
### Roles
 
**Administrador**
 
- Acceso completo a la gestión de usuarios.
 
**Empleado**
 
- Acceso limitado según configuración.
 
**Cliente**
 
- Acceso limitado según configuración.
 
No se implementa un sistema avanzado de permisos, ya que el objetivo es demostrar el uso de eventos en Tkinter.
 
---
 
## Validaciones Implementadas
 
La aplicación valida:
 
- Campos obligatorios.
- Roles válidos.
- Identificadores duplicados.
- Usuarios duplicados.
- Productos duplicados.
- Selecciones vacías.
- Inicio de sesión correcto.
- Datos persistidos correctamente.
 
---
 
## Cómo Ejecutar
 
Desde la carpeta del proyecto:
 
```bash
py main.py
```
 
o
 
```bash
python main.py
```
 
---
 
## Ejemplo de Usuario Administrador
 
```json
{
"identificador": "P001",
"nombre": "Administrador",
"usuario": "Nathaly",
"contrasena": "1234",
"rol": "Administrador"
}
```