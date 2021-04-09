from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse
from loguru import logger

from . import ApiApiClimaTempo


def carregar_exception_api(app: FastAPI):
    """ Tratamento das exceções de api """

    @app.exception_handler(RequestValidationError)
    async def exception_handler_validacao(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={"status": 422, "mensagem": "Os parâmetros da requisição estão inválidos!",
                     "stacktrace": str(exc.raw_errors[0].exc)}
        )

    @app.exception_handler(404)
    def exception_handler_404(request: Request, exc: RequestValidationError):
        logger.error("[-] ENDERECO NAO ENCONTRADO")

        mensagem = exc.mensagem if hasattr(exc, "mensagem") else "Endereço não encontrado!"

        return JSONResponse(
            status_code=404,
            content={"status": 404, "mensagem": mensagem, "stacktrace": ""},
        )

    @app.exception_handler(500)
    def exception_handler_500(request: Request, exc: HTTPException):
        logger.critical(f"[-] ERRO INTERNO: {type(exc).__name__}: {exc}")

        return JSONResponse(
            status_code=500,
            content={"status": 500, "mensagem": "Ocorreu um erro interno!",
                     "stacktrace": f"{type(exc).__name__}: {exc}"})

    @app.exception_handler(ApiApiClimaTempo)
    def exception_handler_api_api_clima_tempo(request: Request, exc: ApiApiClimaTempo):
        logger.error(f"{type(exc).__name__}: {exc.stacktrace} | STACKTRACE: {exc.stacktrace}")

        return JSONResponse(
            status_code=exc.status_code,
            content={"status": exc.status_code, "mensagem": exc.mensagem,
                     "stacktrace": f"{type(exc).__name__}: {exc.stacktrace}" if exc.stacktrace else ""},
        )
