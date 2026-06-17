import requests
from fastapi import HTTPException

from app.config import OPENWEATHER_API_KEY


def consultar_clima(ciudad: str) -> dict:
    if not OPENWEATHER_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="Falta OPENWEATHER_API_KEY en el archivo .env",
        )

    try:
        respuesta = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": ciudad,
                "appid": OPENWEATHER_API_KEY,
                "units": "metric",
                "lang": "es",
            },
            timeout=15,
        )
    except requests.RequestException as error:
        raise HTTPException(
            status_code=502,
            detail=f"No se pudo conectar con OpenWeatherMap: {error}",
        ) from error

    datos = respuesta.json()
    if respuesta.status_code != 200:
        raise HTTPException(
            status_code=respuesta.status_code,
            detail=datos.get("message", "No se pudo obtener el clima"),
        )

    return {
        "ciudad": datos["name"],
        "pais": datos["sys"]["country"],
        "temperatura": datos["main"]["temp"],
        "sensacion_termica": datos["main"]["feels_like"],
        "humedad": datos["main"]["humidity"],
        "descripcion": datos["weather"][0]["description"],
    }
