from pydantic import BaseSettings


class Envs(BaseSettings):
    PROJETO_NOME: str = "API Clima Tempo"
    PROJETO_DESC: str = "A API capturar dados do tempo dos municípios cadastrados"

    class Config:
        case_sensitive = True


envs = Envs()
