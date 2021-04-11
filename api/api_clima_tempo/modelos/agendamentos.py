from datetime import datetime
from typing import List, Optional

from api_clima_tempo.modelos import ResultadoRetorno
from pydantic import BaseModel, Field


class Agendamento(BaseModel):
    proxima_execucao: Optional[datetime] = Field(..., description="Data da proxima execução")
    intervalo: Optional[int] = Field(60, description="Intervalo entre as execuções em minutos", ge=30)


class ResultadoBuscarAgendamentos(ResultadoRetorno):
    resultado: List[Agendamento]
