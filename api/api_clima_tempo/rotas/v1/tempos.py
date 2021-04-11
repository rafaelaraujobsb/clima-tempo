from fastapi import APIRouter, Path, Query

from api_clima_tempo.modelos import MODEL_RESPOSTAS_DEFAULT
from api_clima_tempo.modelos.tempos import ResultadoBuscarTempo
from api_clima_tempo.modulos.tempos import listar
from api_clima_tempo.modulos.utils import parse_openapi


rota = APIRouter()


@rota.get("/", status_code=200, summary="Rota Listar Tempos", responses=parse_openapi(MODEL_RESPOSTAS_DEFAULT),
          response_model=ResultadoBuscarTempo)
def rota_get_tempos(inicio: int = Query(1, description="Posição inicial da paginação", ge=1),
                    quantidade: int = Query(100, description="Quantidade de registros", ge=1, le=100)):
    """ Listar tempos dos municipios cadastrados """
    resultado, paginacao = listar(inicio=inicio, quantidade=quantidade)

    return ResultadoBuscarTempo(status=200, resultado=resultado, paginacao=paginacao)


@rota.get("/{estado}", status_code=200, summary="Rota Listar Tempos", responses=parse_openapi(MODEL_RESPOSTAS_DEFAULT),
          response_model=ResultadoBuscarTempo)
def rota_get_tempos_estado(estado: str = Path(..., description="Sigla do estado"),
                           inicio: int = Query(1, description="Posição inicial da paginação", ge=1),
                           quantidade: int = Query(100, description="Quantidade de registros", ge=1, le=100)):
    """ Listar tempos dos municipios de um estado  """
    resultado, paginacao = listar(inicio=inicio, quantidade=quantidade, estado=estado)

    return ResultadoBuscarTempo(status=200, resultado=resultado, paginacao=paginacao)


@rota.get("/{estado}/{municipio}", status_code=200, summary="Rota Listar Tempos",
          responses=parse_openapi(MODEL_RESPOSTAS_DEFAULT), response_model=ResultadoBuscarTempo)
def rota_get_tempos_municipios(estado: str = Path(..., description="Sigla do estado"),
                               municipio: str = Path(..., description="Municipio do estado"),
                               inicio: int = Query(1, description="Posição inicial da paginação", ge=1),
                               quantidade: int = Query(100, description="Quantidade de registros", ge=1, le=100)):
    """ Listar tempos do municipio """
    resultado, paginacao = listar(inicio=inicio, quantidade=quantidade, estado=estado, municipio=municipio)

    return ResultadoBuscarTempo(status=200, resultado=resultado, paginacao=paginacao)
