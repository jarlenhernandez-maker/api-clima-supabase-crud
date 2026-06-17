from fastapi import APIRouter, HTTPException, Path

from app.config import TABLE_NAME
from app.database import get_supabase
from app.schemas import ConsultaCreate, ConsultaUpdate
from app.services.weather import consultar_clima


router = APIRouter()


@router.get("/api", summary="Endpoint de bienvenida en JSON")
def api_inicio():
    return {
        "mensaje": "API CRUD de clima funcionando",
        "documentacion": "/docs",
        "vista_web": "/",
        "endpoints": [
            "GET /clima/{ciudad}",
            "POST /consultas",
            "GET /consultas",
            "GET /consultas/{consulta_id}",
            "PUT /consultas/{consulta_id}",
            "DELETE /consultas/{consulta_id}",
        ],
    }


@router.get("/clima/{ciudad}", summary="Consultar clima sin guardar en Supabase")
def clima(ciudad: str = Path(..., min_length=2, examples=["Bogota"])):
    return consultar_clima(ciudad)


@router.post("/consultas", summary="Crear una consulta climatica en Supabase")
def crear_consulta(payload: ConsultaCreate):
    clima_actual = consultar_clima(payload.ciudad)
    registro = {**clima_actual, "notas": payload.notas}

    respuesta = get_supabase().table(TABLE_NAME).insert(registro).execute()
    if not respuesta.data:
        raise HTTPException(status_code=500, detail="No se pudo crear el registro")
    return respuesta.data[0]


@router.get("/consultas", summary="Leer todas las consultas guardadas")
def listar_consultas():
    respuesta = (
        get_supabase()
        .table(TABLE_NAME)
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )
    return respuesta.data


@router.get("/consultas/{consulta_id}", summary="Leer una consulta por ID")
def obtener_consulta(consulta_id: str):
    respuesta = (
        get_supabase()
        .table(TABLE_NAME)
        .select("*")
        .eq("id", consulta_id)
        .single()
        .execute()
    )
    if not respuesta.data:
        raise HTTPException(status_code=404, detail="Consulta no encontrada")
    return respuesta.data


@router.put("/consultas/{consulta_id}", summary="Actualizar una consulta guardada")
def actualizar_consulta(consulta_id: str, payload: ConsultaUpdate):
    cambios = payload.model_dump(exclude_unset=True)
    if not cambios:
        raise HTTPException(status_code=400, detail="No enviaste datos para actualizar")

    if payload.ciudad:
        clima_actual = consultar_clima(payload.ciudad)
        cambios.update(clima_actual)

    respuesta = (
        get_supabase()
        .table(TABLE_NAME)
        .update(cambios)
        .eq("id", consulta_id)
        .execute()
    )
    if not respuesta.data:
        raise HTTPException(status_code=404, detail="Consulta no encontrada")
    return respuesta.data[0]


@router.delete("/consultas/{consulta_id}", summary="Eliminar una consulta guardada")
def eliminar_consulta(consulta_id: str):
    respuesta = (
        get_supabase()
        .table(TABLE_NAME)
        .delete()
        .eq("id", consulta_id)
        .execute()
    )
    if not respuesta.data:
        raise HTTPException(status_code=404, detail="Consulta no encontrada")
    return {"mensaje": "Consulta eliminada", "registro": respuesta.data[0]}
