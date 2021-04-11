import traceback

from loguru import logger

from scrapper_clima_tempo import celery
from scrapper_clima_tempo.exceptions import Falha
from scrapper_clima_tempo.servicos.scrapper import ScrapperClimaTempo
from scrapper_clima_tempo.servicos.database import CollectionTempos, CollectionExecucoes


@celery.task(name="scrapper.task_buscar_clima")
def task_buscar_clima(estado: str, municipio: str):
    logger.info(f"TASK {task_buscar_clima.name} INICIADA")

    with CollectionExecucoes() as collection_execucoes:
        id_execucao = collection_execucoes.cadastar(estado=estado, municipio=municipio)

    erro = None

    try:
        clima = ScrapperClimaTempo().buscar_clima(estado=estado, municipio=municipio)
    except Falha as error:
        erro = {"mensagem": error.mensagem, "stacktrace": error.stacktrace}
    except Exception:
        erro = {"mensagem": "Ocorreu um erro inesperado!", "stacktrace": traceback.format_exc()}
        logger.critical(f"TASK {task_buscar_clima.name} ERRO INESPERADO: {estado} - {municipio}")
    finally:
        with CollectionExecucoes() as collection_execucoes:
            collection_execucoes.atualizar(id_execucao, erro=erro)

        if not erro:
            with CollectionTempos() as collection_climas:
                collection_climas.cadastar(estado=estado, municipio=municipio, **clima)

    logger.info(f"TASK {task_buscar_clima.name} FINALIZADA")
