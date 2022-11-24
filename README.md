# VSM-SNW 

Sitio Web para Santillana Contigo

## Requerimientos:

- Docker
- Docker compose

## Desarrollo

El proyecto se configura por medio de variables de ambiente. Está desarrollado para 
leer los archivos `.env` de cada contenedor y el principal del proyecto. Para ver las
opciones disponibles puede guiarse por los archivos `.env.example`.

### Generar los archivos de configuración en git Bash

```shell
$ docker run -ti --rm -v "c:/ruta/a/carpeta/del/proyecto":"/var/lib/dotenver/" jmfederico/dotenver
```

### Generar los archivos de configuración en Windows cmd

```shell
$ docker run -ti --rm -v "c:\ruta\a\carpeta\del\proyecto":"/var/lib/dotenver/" jmfederico/dotenver
```

### Generar los archivos de configuración en Mac, Linux o WSL

```shell
$ docker run -ti --rm -v "${PWD}:/var/lib/dotenver/" jmfederico/dotenver
```

### Levantar Docker

```shell
$ docker-compose build
$ docker-compose up -d
```

### Otras operaciones con Docker
```shell
# Reiniciar el contenedor
$ docker-compose restart contenedor
# Detener el contenedor
$ docker-compose stop contenedor
```

Para ejecutar algo en todos los contenedores se realiza de la misma manera sin 
especificar el contenedor al final del comando.

### Ejecutar comandos en Django

```shell
# Crear un superusuario
$ docker-compose run --rm django ./manage.py createsuperuser
# Crear migraciones
$ docker-compose run --rm django ./manage.py makemigrations
# Ejecutar migraciones
$ docker-compose run --rm django ./manage.py migrate
```

La aplicación estará disponible en: https://localhost

## Uso de poetry dentro del contenedor

### Agregar una dependencia al proyecto

```shell
$ docker-compose run --rm django poetry add nombre_paquete
```

### Actualizar las dependencias del proyecto

```shell
$ docker-compose run --rm django poetry update
```

### Eliminar una dependencia del proyecto

```shell
$ docker-compose run --rm django poetry remove nombre_paquete
```

## Transpilación de Sass

En su ambiente de desarrollo las transpilaciones de sass a css se realizan 
automaticamente. Si requiere incluir sass en su template recuerde cargar el 
templatetag e incluir su archivo en el bloque extra_css.

```
{% load snw_sass %}
{% block inline_css %}
  {# inside ui/ #}
  <link href="{% sass_src 'main_theme.scss' %}" rel="stylesheet" type="text/css" />
{% endblock %}
```

La unica carpeta que se escanea en busca de estilos es `ui`

Si desea transpilar manualmente los archivos `.scss`
```
$ docker-compose run --rm django ./manage.py compilescss
```
#### **Nota**:
>Actualmente no es necesario ejecutar este comando, puesto que los archivos son transpilados automaticamente en el momento de publicar.
Dicho esto, es recomendable que usted no realice commit de los archivos `.css` y `.map` generados en su ambiente local.

## Puertos

| Servicio | contenedor | host        |
|----------|------------|-------------|
| Django   | 8000       | 8000        |
| Postgres | 5432       | 5432        |
| Caddy    | 80, 443    | 80, 443     |
| maildev  | 1080, 1025 | 1080, 1025  |
| vite     | 3000, 9000 | 3000, 9000  |

