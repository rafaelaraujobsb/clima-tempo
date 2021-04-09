from pydantic import BaseModel, Field


class __Status(BaseModel):
    status: int = Field(..., description="status_code da requisição")


class MensagemRetorno(__Status):
    mensagem: str = Field(..., description="Mensagem sobre a requisição")
    stacktrace: str = Field(..., description="Stacktrace do erro para casos não tratados")


class ResultadoRetorno(__Status):
    pass


class Paginacao(BaseModel):
    anterior: int = Field(..., description="A partir de qual registro que começou o resultado anterior")
    proximo: int = Field(None, description="A partir de qual registro começa a nova busca")

    class Config:
        schema_extra = {
            "example": {
                "anterior": 10,
                "proximo": 100
            }
        }


# Models Resposta Default
MODEL_RESPOSTAS_DEFAULT = {
    422: MensagemRetorno(status=422, mensagem="Os parâmetros da requisição estão inválidos!", stacktrace=""),
    500: MensagemRetorno(status=500, mensagem="Ocorreu um erro interno!",
                         stacktrace="func() takes 0 positional arguments but 2 were given"),
}
