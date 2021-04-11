from fastapi import APIRouter

from .v1 import agendamentos, execucoes, municipios, tempos  # noqa


rota_v1 = APIRouter()
rota_v1.include_router(agendamentos.rota, prefix="/agendamentos", tags=["Agendamentos"])
rota_v1.include_router(execucoes.rota, prefix="/execucoes", tags=["Execucoes"])
rota_v1.include_router(municipios.rota, prefix="/municipios", tags=["Municípios"])
rota_v1.include_router(tempos.rota, prefix="/tempos", tags=["Tempos"])
