from typing import Optional

from pydantic import BaseModel, Field


class ConsultaCreate(BaseModel):
    ciudad: str = Field(..., min_length=2, examples=["Bogota"])
    notas: Optional[str] = Field(None, max_length=250, examples=["Consulta para clase"])


class ConsultaUpdate(BaseModel):
    ciudad: Optional[str] = Field(None, min_length=2, examples=["Medellin"])
    notas: Optional[str] = Field(None, max_length=250, examples=["Actualizado desde Swagger"])
