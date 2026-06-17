from fastapi import HTTPException
from supabase import Client, create_client

from app.config import SUPABASE_KEY, SUPABASE_URL


def get_supabase() -> Client:
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise HTTPException(
            status_code=500,
            detail="Faltan SUPABASE_URL o SUPABASE_KEY en el archivo .env",
        )
    return create_client(SUPABASE_URL, SUPABASE_KEY)
