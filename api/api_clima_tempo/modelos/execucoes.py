from datetime import datetime
from typing import List

from api_clima_tempo.modelos import Paginacao, ResultadoRetorno
from api_clima_tempo.modelos.municipios import Municipio
from api_clima_tempo.modelos.tasks import Status
from pydantic import BaseModel, Field


class Erro(BaseModel):
    mensagem: str = Field(..., description="HTML da página do erro")
    stacktrace: str = Field(None, description="Stacktrace do erro, se for um erro"
                                              " na requisição será apresentado o HTML")


class Execucao(Municipio):
    data_inicio: datetime = Field(..., description="Data que começou a execução")
    data_fim: datetime = Field(None, description="Data que terminou a execução")
    status: Status = Field(..., description="Status do processamento")
    erro: Erro = Field(None, description="Erro que ocorreu no processamento")


class ResultadoBuscarExecucoes(ResultadoRetorno):
    resultado: List[Execucao]
    paginacao: Paginacao
