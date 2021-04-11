from datetime import datetime, timedelta

from loguru import logger

from scrapper_clima_tempo import celery
from scrapper_clima_tempo.modulos.scrapper import task_buscar_clima
from scrapper_clima_tempo.servicos.database import CollectionAgendamento, CollectionMunicipios


@celery.task(name="schedule.task_scheduler")
def task_scheduler():
    logger.info(f"TASK {task_scheduler.name} INICIADA")

    with CollectionAgendamento() as collection_agendamento:
        agendamento = collection_agendamento.buscar()

    if agendamento:
        if agendamento["proxima_execucao"] and agendamento["proxima_execucao"] <= datetime.now():
            with CollectionMunicipios() as collection_municipios:
                for registro in collection_municipios.listar_cursor():
                    task_buscar_clima.apply_async(kwargs={"estado": registro["estado"],
                                                          "municipio": registro["municipio"]})
                    logger.info(f'[+] ({registro["estado"]}, {registro["municipio"]} NA FILA')

            with CollectionAgendamento() as collection_agendamento:
                proxima_execucao = datetime.now() + timedelta(minutes=agendamento["intervalo"])
                agendamento = collection_agendamento.atualizar(data=proxima_execucao,
                                                               intervalo=agendamento["intervalo"])
    else:
        logger.warning(f"TASK {task_scheduler.name} NENHUM AGENDAMENTO")

    logger.info(f"TASK {task_scheduler.name} FINALIZADA")
