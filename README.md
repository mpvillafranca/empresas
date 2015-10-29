# empresas
>Tema 2: ejercicio 2. IV-2015-2016

Uso:
- Crear entorno virtual en la carpeta del proyecto e instalar dependencias
    virtualenv .
    pip install -r requirements/local.txt
- Ingresar en la aplicación
    cd src
- Sincronizar la base de datos y lanzar el servidor
    python manage.py syncdb --settings=ValoracionEmpresas.settings.local
    python manage.py runserver --settings=ValoracionEmpresas.settings.local
