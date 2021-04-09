from fastapi import HTTPException


class ApiApiClimaTempo(HTTPException):
    """ Classe Base """

    def __init__(self, status_code: int, mensagem: str, stacktrace: str = ""):
        self.mensagem = mensagem
        self.stacktrace = stacktrace
        self.status_code = status_code

    def __repr__(self):
        return f"\n---> Status: {self.status}\n---> Mensagem: {self.mensagem}\n---> Stacktrace: {self.stacktrace}"

    def __str__(self):
        return self.mensagem


class DadoInvalido(ApiApiClimaTempo):
    def __init__(self, mensagem: str = "Dado inválido!", stacktrace: str = ""):
        super().__init__(status_code=406, mensagem=mensagem, stacktrace=stacktrace)


class RegistroJaInserido(ApiApiClimaTempo):
    def __init__(self, mensagem: str = "Registro já inserido!", stacktrace: str = ""):
        super().__init__(status_code=409, mensagem=mensagem, stacktrace=stacktrace)


class RegistroNaoEncontrado(ApiApiClimaTempo):
    def __init__(self, mensagem: str = "Registro não encontrado!", stacktrace: str = ""):
        super().__init__(status_code=404, mensagem=mensagem, stacktrace=stacktrace)


class Proibido(ApiApiClimaTempo):
    def __init__(self, mensagem: str = "Operação não permitida!", stacktrace: str = ""):
        super().__init__(status_code=403, mensagem=mensagem, stacktrace=stacktrace)


class Falha(ApiApiClimaTempo):
    def __init__(self, mensagem: str = "Operação não realizada!", stacktrace: str = ""):
        super().__init__(status_code=400, mensagem=mensagem, stacktrace=stacktrace)
