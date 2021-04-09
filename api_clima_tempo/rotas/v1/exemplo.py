from fastapi import APIRouter

from ...modelos import MensagemRetorno, MODEL_RESPOSTAS_DEFAULT
from ...modulos.utils import parse_openapi


rota = APIRouter()


@rota.get("/", summary="Rota Exemplo GET", responses=parse_openapi(MODEL_RESPOSTAS_DEFAULT))
def rota_exemplo():
    """ Docs exemplo

    Essa é uma doc de exemplo.<br>
    **Exemplo:** 123
    """
    return MensagemRetorno(status=200, mensagem="Teste", stacktrace="")
