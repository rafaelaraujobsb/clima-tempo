from fastapi import APIRouter

from .v1 import exemplo  # noqa


rota_v1 = APIRouter()
rota_v1.include_router(exemplo.rota, prefix="/exemplo", tags=["Exemplo"])
