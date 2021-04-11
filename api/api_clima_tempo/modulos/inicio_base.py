from api_clima_tempo.servicos.database import (
    CollectionAgendamento, CollectionTempos, CollectionExecucoes, CollectionMunicipios
)


def criar_indexes():
    for collection in [CollectionAgendamento, CollectionTempos, CollectionExecucoes, CollectionMunicipios]:
        collection().criar_index()


def carregar_base():
    for collection in [CollectionAgendamento]:
        collection().carregar_base()
