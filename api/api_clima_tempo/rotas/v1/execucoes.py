from fastapi import APIRouter, Query

from api_clima_tempo.modelos import MODEL_RESPOSTAS_DEFAULT
from api_clima_tempo.modelos.execucoes import ResultadoBuscarExecucoes
from api_clima_tempo.modulos.execucoes import listar
from api_clima_tempo.modulos.utils import parse_openapi


rota = APIRouter()


@rota.get("/", status_code=200, summary="Rota Listar Execuções", responses=parse_openapi(MODEL_RESPOSTAS_DEFAULT),
          response_model=ResultadoBuscarExecucoes)
def rota_get_execucoes(inicio: int = Query(1, description="Posição inicial da paginação", ge=1),
                       quantidade: int = Query(100, description="Quantidade de registros", ge=1, le=100)):
    """ Listar Execuções """
    resultado, paginacao = listar(inicio=inicio, quantidade=quantidade)

    return ResultadoBuscarExecucoes(status=200, resultado=resultado, paginacao=paginacao)
