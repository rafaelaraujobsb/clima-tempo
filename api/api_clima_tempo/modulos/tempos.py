from api_clima_tempo.servicos.database import CollectionTempos
from api_clima_tempo.modulos.utils import montar_paginacao


def listar(*, inicio: int, quantidade: int, estado: str = None, municipio: str = None) -> tuple:
    with CollectionTempos() as collection_tempos:
        resultado = collection_tempos.listar(inicio=inicio, quantidade=quantidade+1, estado=estado, municipio=municipio)
        id_anterior = collection_tempos.buscar_anterior(inicio=inicio)

    paginacao = montar_paginacao(resultado=resultado, anterior=id_anterior, quantidade=quantidade,
                                 chave_proximo="id_tempo")

    return resultado, paginacao
