from fastapi import APIRouter

from api_clima_tempo.modelos import MensagemRetorno, MODEL_RESPOSTAS_DEFAULT
from api_clima_tempo.modelos.agendamentos import Agendamento, ResultadoBuscarAgendamentos
from api_clima_tempo.modulos.agendamentos import atualizar, buscar
from api_clima_tempo.modulos.utils import parse_openapi
from api_clima_tempo.exceptions import MensagemStatusCode


rota = APIRouter()


@rota.put("/", status_code=201, summary="Rota Atualizar Agendamento", responses=parse_openapi(MODEL_RESPOSTAS_DEFAULT),
          response_model=MensagemRetorno)
def rota_put_agendamento(agendamento: Agendamento):
    """ Agendar a execução do scrapper """
    if not atualizar(**agendamento.dict()):
        raise MensagemStatusCode(status_code=200, mensagem="Agendamento não atualizado!")

    return MensagemRetorno(status=201, mensagem="Agendamento atualizado!", stacktrace="")


@rota.get("/", status_code=200, summary="Rota Buscar Agendamento", responses=parse_openapi(MODEL_RESPOSTAS_DEFAULT),
          response_model=ResultadoBuscarAgendamentos)
def rota_get_agendamento():
    """ Listar Agendamentos """
    return ResultadoBuscarAgendamentos(status=200, resultado=buscar())
