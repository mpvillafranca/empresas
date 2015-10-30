# empresas
>Tema 2: ejercicio 2. IV-2015-2016

[![Build Status](https://travis-ci.org/mpvillafranca/empresas.svg?branch=master)](https://travis-ci.org/mpvillafranca/empresas)

*Aplicación para calificar las empresas en las que hacen prácticas los alumnos. Las acciones permitidas son crear empresa y listar calificaciones para cada empresa, crear calificación y añadirla (comprobando que la persona no la haya añadido ya), borrar calificación (si se arrepiente o te denuncia la empresa o algo) y hacer un ránking de empresas por calificación.*

Uso:
- Crear entorno virtual en la carpeta del proyecto e instalar dependencias

        virtualenv .
        pip install -r requirements/local.txt
- Ingresar en la aplicación

        cd src
- Sincronizar la base de datos y lanzar el servidor

        python manage.py syncdb --settings=ValoracionEmpresas.settings.local
        python manage.py runserver --settings=ValoracionEmpresas.settings.local
        
- Acceder desde el navegador a:

        http://localhost:8000
