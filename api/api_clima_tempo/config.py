from pydantic import BaseSettings

from api_clima_tempo.servicos.mod_database import TipoConexao


class Envs(BaseSettings):
    PROJETO_NOME: str = "API Clima Tempo"
    PROJETO_DESC: str = "API para expor os dados de agendamento, execução e informações dos municípios do scrapper" \
                        "<br>**Swagger:** `/swagger`<br>**OpenAPI:** `/docs`"

    MONGO_DB: str = "climatempo"
    MONGO_USR: str
    MONGO_PWD: str
    MONGO_HOST: str
    MONGO_PORT: str = 27017
    MONGO_TIPO_CON: TipoConexao = TipoConexao.MONGODB

    class Config:
        case_sensitive = True


envs = Envs()
