from datetime import datetime

from api_clima_tempo.servicos.database import CollectionAgendamento


def atualizar(proxima_execucao: datetime, intervalo: int) -> int:
    with CollectionAgendamento() as collection_agendamento:
        resultado = collection_agendamento.atualizar(data=proxima_execucao, intervalo=intervalo)

    return resultado


def buscar() -> list:
    with CollectionAgendamento() as collection_agendamento:
        resultado = collection_agendamento.buscar()

    return [resultado]
