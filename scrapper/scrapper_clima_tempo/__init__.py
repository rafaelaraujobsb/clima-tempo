import urllib3
from celery import Celery
from loguru import logger

from scrapper_clima_tempo import celeryconfig
from scrapper_clima_tempo.modulos.inicio_base import carregar_base, criar_indexes


urllib3.disable_warnings()

# Versão
__version__ = "0.3.0"

logger.add("critico.log", level="CRITICAL", retention="60 days")
logger.add("debug.log", level="DEBUG", retention="60 days")
logger.add("error.log", level="ERROR", retention="60 days")
logger.add("info.log", level="INFO", retention="60 days")

# Inicio Base
carregar_base()
criar_indexes()

celery = Celery("clima_tempo")
celery.config_from_object(celeryconfig)
