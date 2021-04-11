from datetime import datetime
from typing import List

from api_clima_tempo.modelos import Paginacao, ResultadoRetorno
from api_clima_tempo.modelos.municipios import Municipio
from pydantic import BaseModel, Field


class Tempo(BaseModel):
    umidade: int
    pressao: int
    vento: int
    temperatura: int


class TempoMunicipio(Municipio):
    tempo: Tempo = Field(..., description="Dados do tempo do municipio")
    data_cadastro: datetime = Field(..., description="Data que o tempo foi cadastrado")


class ResultadoBuscarTempo(ResultadoRetorno):
    resultado: List[TempoMunicipio]
    paginacao: Paginacao
