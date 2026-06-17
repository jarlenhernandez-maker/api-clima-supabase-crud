# API CRUD de Clima con FastAPI y Supabase

Este proyecto implementa una API en Python usando FastAPI. La API consulta el clima actual en OpenWeatherMap y permite hacer CRUD completo en una tabla de Supabase:

- Crear registros de consultas climaticas.
- Leer todos los registros.
- Leer un registro por ID.
- Actualizar ciudad o notas de un registro.
- Eliminar registros.

## Tecnologias

- Python
- FastAPI
- Supabase
- OpenWeatherMap
- Swagger UI automatico

## Estructura

```text
api_clima_supabase/
  main.py
  app/
    __init__.py
    config.py
    database.py
    schemas.py
    routes/
      api.py
      pages.py
    services/
      weather.py
  templates/
    index.html
  requirements.txt
  .env.example
  supabase_schema.sql
  README.md
```

## Organizacion del codigo

- `main.py`: punto de entrada. Crea la aplicacion importando `create_app`.
- `app/__init__.py`: configura FastAPI y registra las rutas.
- `app/config.py`: lee las variables del archivo `.env`.
- `app/database.py`: crea la conexion con Supabase.
- `app/schemas.py`: define los modelos de datos para crear y actualizar.
- `app/services/weather.py`: consume la API externa de OpenWeatherMap.
- `app/routes/api.py`: contiene los endpoints del CRUD.
- `app/routes/pages.py`: entrega la vista web principal.
- `templates/index.html`: contiene la interfaz visual del proyecto.

## 1. Crear la tabla en Supabase

1. Entra a tu proyecto de Supabase.
2. Abre SQL Editor.
3. Copia y ejecuta el contenido de `supabase_schema.sql`.

La tabla creada se llama `consultas_clima`.

## 2. Configurar variables de entorno

Copia `.env.example` como `.env`:

```bash
copy .env.example .env
```

Edita `.env` y agrega:

```env
OPENWEATHER_API_KEY=tu_api_key_de_openweathermap
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_KEY=tu_anon_key_de_supabase
```

En Supabase encuentras `SUPABASE_URL` y `SUPABASE_KEY` en:

```text
Project Settings > API
```

## 3. Instalar dependencias

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 4. Ejecutar el proyecto

```bash
uvicorn main:app --reload
```

Luego abre:

```text
http://127.0.0.1:8000/
```

Esa es la vista web del proyecto. Tambien puedes abrir Swagger para probar la API tecnicamente:

```text
http://127.0.0.1:8000/docs
```

## Despliegue en Render

El repositorio incluye `render.yaml` para crear el servicio web en Render.

Configuracion esperada:

```text
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
```

En Render se deben crear estas variables de entorno:

```env
OPENWEATHER_API_KEY=tu_api_key_de_openweathermap
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_KEY=tu_key_publica_o_anon
```

No subas el archivo `.env` a GitHub. Ese archivo solo se usa localmente.

## Endpoints principales

| Metodo | Ruta | Descripcion |
| --- | --- | --- |
| GET | `/` | Muestra la vista web del proyecto |
| GET | `/api` | Verifica que la API funciona en formato JSON |
| GET | `/clima/{ciudad}` | Consulta clima sin guardar |
| POST | `/consultas` | Crea una consulta y la guarda en Supabase |
| GET | `/consultas` | Lista todas las consultas |
| GET | `/consultas/{consulta_id}` | Obtiene una consulta por ID |
| PUT | `/consultas/{consulta_id}` | Actualiza una consulta |
| DELETE | `/consultas/{consulta_id}` | Elimina una consulta |

## Ejemplo para crear registro

En Swagger, abre `POST /consultas` y envia:

```json
{
  "ciudad": "Bogota",
  "notas": "Consulta creada desde Swagger"
}
```

La API consulta OpenWeatherMap, arma el registro y lo guarda en Supabase.

## Explicacion corta del flujo

1. El usuario envia una ciudad.
2. FastAPI consulta OpenWeatherMap.
3. La API recibe temperatura, humedad, pais y descripcion.
4. El registro se guarda en Supabase.
5. Los otros endpoints permiten leer, actualizar o eliminar esos datos.
