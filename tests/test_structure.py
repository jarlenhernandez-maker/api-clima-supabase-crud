from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_project_files_exist():
    assert (ROOT / "main.py").exists()
    assert (ROOT / "app" / "routes" / "api.py").exists()
    assert (ROOT / "app" / "services" / "weather.py").exists()
    assert (ROOT / "templates" / "index.html").exists()
    assert (ROOT / "requirements.txt").exists()
    assert (ROOT / ".env.example").exists()
    assert (ROOT / "supabase_schema.sql").exists()


def test_crud_routes_are_declared():
    source = (ROOT / "app" / "routes" / "api.py").read_text(encoding="utf-8")
    assert '@router.post("/consultas"' in source
    assert '@router.get("/consultas"' in source
    assert '@router.get("/consultas/{consulta_id}"' in source
    assert '@router.put("/consultas/{consulta_id}"' in source
    assert '@router.delete("/consultas/{consulta_id}"' in source
