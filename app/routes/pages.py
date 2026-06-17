from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter()


@router.get("/", response_class=HTMLResponse, summary="Vista web del proyecto")
def inicio():
    template_path = Path(__file__).resolve().parents[2] / "templates" / "index.html"
    return template_path.read_text(encoding="utf-8")
