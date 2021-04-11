from pydantic import BaseSettings

from scrapper_clima_tempo.servicos.mod_database import TipoConexao


class Envs(BaseSettings):
    URL_CLIMATEMPO: str = "https://www.tempoagora.com.br/previsao-do-tempo"

    MONGO_DB: str = "climatempo"
    MONGO_USR: str
    MONGO_PWD: str
    MONGO_HOST: str
    MONGO_PORT: str = 27017
    MONGO_TIPO_CON: TipoConexao = TipoConexao.MONGODB

    BROKER: str = ""

    TS_SCHEDULE: int = 1

    class Config:
        case_sensitive = True


envs = Envs()
