from fastapi import APIRouter, Query

from api_clima_tempo.modelos import MensagemRetorno, MODEL_RESPOSTAS_DEFAULT
from api_clima_tempo.modelos.municipios import Municipio, ResultadoBuscarMunicipios
from api_clima_tempo.modulos.municipios import cadastrar, listar, remover
from api_clima_tempo.modulos.utils import parse_openapi
from api_clima_tempo.exceptions import MensagemStatusCode


rota = APIRouter()


@rota.get("/", status_code=200, summary="Rota Listar Municipio", responses=parse_openapi(MODEL_RESPOSTAS_DEFAULT),
          response_model=ResultadoBuscarMunicipios)
def rota_get_municipios(inicio: int = Query(1, description="Posição inicial da paginação", ge=1),
                        quantidade: int = Query(100, description="Quantidade de registros", ge=1, le=100)):
    """ Listar os municipios cadastrados """
    resultado, paginacao = listar(inicio=inicio, quantidade=quantidade)

    return ResultadoBuscarMunicipios(status=200, resultado=resultado, paginacao=paginacao)


@rota.post("/", status_code=201, summary="Rota Cadastrar Municipio", responses=parse_openapi(MODEL_RESPOSTAS_DEFAULT),
           response_model=MensagemRetorno)
def rota_post_municipios(municipio: Municipio):
    """ Cadastrar Municpio """
    if not cadastrar(**municipio.dict()):
        raise MensagemStatusCode(status_code=200, mensagem="Municipio não cadastrado!")

    return MensagemRetorno(status=201, mensagem="Municipio cadastrado!", stacktrace="")


@rota.delete("/{id_municipio}", status_code=201, summary="Rota Agendamento",
             responses=parse_openapi(MODEL_RESPOSTAS_DEFAULT), response_model=MensagemRetorno)
def rota_delete_municipios(id_municipio: int):
    """ Remover Municpio """
    if not remover(id_municipio):
        raise MensagemStatusCode(status_code=200, mensagem="Municipio não removido!")

    return MensagemRetorno(status=201, mensagem="Municipio removido!", stacktrace="")
