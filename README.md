# Tercera-pre-entrega-Murua

Para levantar la app debe hacer lo siguiente:

- abrir consola (Powershell para Windows)
- Instalar el paquete de ambiente virtual en caso de no tenerlo -> pip install virtualenv
- Ubicado dentro de la carpeta src -> virtualenv venv (creamos el ambiente virtual)
- Activar el ambiente virtual creado -> venv\Scripts\activate
- Una vez dentro del ambiente, levantar el servidor -> pýthon manage.py runserver

Funcionalidades:

- En la ruta principal http://127.0.0.1:8000/ -> inputs de busqueda (productos, ofertas, vendedor y comprador)

Rutas secundarias:
Se acceden desde los botones de la barra de navegacion (Vendedores - Productos - Compradores - Ofertas)

- En la ruta de vendedores http://127.0.0.1:8000/vendedores/ -> Formulario de creacion de vendedor y visualizacion de todos los vendedores registrados en la base de datos

- En la ruta de compradores http://127.0.0.1:8000/compradores/ -> Formulario de creacion de comprador y visualizacion de todos los compradores registrados en la base de datos

- En la ruta de productos http://127.0.0.1:8000/productos/ -> Formulario de creacion de productos y visualizacion de todos los productos registrados en la base de datos

- En la ruta de ofertas http://127.0.0.1:8000/ofertas/ -> Formulario de creacion de ofertas y visualizacion de todas las ofertas registradas en la base de datos