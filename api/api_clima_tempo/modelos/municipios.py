from datetime import datetime
from typing import List

from api_clima_tempo.modelos import Paginacao, ResultadoRetorno
from pydantic import BaseModel, Field, validator


ESTADOS = {"ac", "al", "ap", "am", "ba", "ce", "df", "es", "go", "ma", "mt", "ms", "mg", "pa", "pb", "pr", "pe", "pi",
           "rj", "rn", "rs", "ro", "rr", "sc", "sp", "se", "to"}


class Municipio(BaseModel):
    estado: str = Field(..., description="Silga do estado do municipio")
    municipio: str = Field(..., description="Nome do municipio")

    @validator("estado")
    def validar_estado(cls, v: str):
        v = v.lower()

        if v not in ESTADOS:
            raise ValueError("Estado inválido")

        return v

    @validator("municipio")
    def validar_municipio(cls, v: str):
        return v.lower()


class MunicipioDB(Municipio):
    id_municipio: int = Field(..., description="Data da proxima execução")
    data_cadastro: datetime = Field(..., description="Data do cadastro")


class ResultadoBuscarMunicipios(ResultadoRetorno):
    resultado: List[MunicipioDB]
    paginacao: Paginacao
