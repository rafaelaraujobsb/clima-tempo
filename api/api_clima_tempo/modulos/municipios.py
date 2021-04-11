from api_clima_tempo.exceptions import RegistroJaInserido
from api_clima_tempo.servicos.database import CollectionMunicipios
from api_clima_tempo.modulos.utils import montar_paginacao


def cadastrar(*, estado: str, municipio: str) -> int:
    with CollectionMunicipios() as collection_municipios:
        if collection_municipios.buscar(estado=estado, municipio=municipio):
            raise RegistroJaInserido("Estado e municipio já cadastrado!")

        resultado = collection_municipios.cadastar(estado=estado, municipio=municipio)

    return resultado


def listar(*, inicio: int, quantidade: int) -> tuple:
    with CollectionMunicipios() as collection_municipios:
        resultado = collection_municipios.listar(inicio=inicio, quantidade=quantidade+1)
        id_anterior = collection_municipios.buscar_anterior(inicio=inicio)

    paginacao = montar_paginacao(resultado=resultado, anterior=id_anterior, quantidade=quantidade,
                                 chave_proximo="id_municipio")

    return resultado, paginacao


def remover(id_municipio: int) -> int:
    with CollectionMunicipios() as collection_municipios:
        resultado = collection_municipios.remover(id_municipio)

    return resultado
