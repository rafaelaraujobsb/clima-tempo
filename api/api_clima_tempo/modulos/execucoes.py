from api_clima_tempo.servicos.database import CollectionExecucoes
from api_clima_tempo.modulos.utils import montar_paginacao


def listar(*, inicio: int, quantidade: int) -> tuple:
    with CollectionExecucoes() as collection_execucoes:
        resultado = collection_execucoes.listar(inicio=inicio, quantidade=quantidade+1)
        id_anterior = collection_execucoes.buscar_anterior(inicio=inicio)

    paginacao = montar_paginacao(resultado=resultado, anterior=id_anterior, quantidade=quantidade,
                                 chave_proximo="id_tempo")

    return resultado, paginacao
