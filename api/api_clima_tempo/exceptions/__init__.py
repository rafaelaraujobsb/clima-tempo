from fastapi import HTTPException


class ApiClimaTempo(HTTPException):
    """ Classe Base """

    def __init__(self, status_code: int, mensagem: str, stacktrace: str = ""):
        self.mensagem = mensagem
        self.stacktrace = stacktrace
        self.status_code = status_code

    def __repr__(self):
        return f"\n---> Status: {self.status}\n---> Mensagem: {self.mensagem}\n---> Stacktrace: {self.stacktrace}"

    def __str__(self):
        return self.mensagem


class DadoInvalido(ApiClimaTempo):
    def __init__(self, mensagem: str = "Dado inválido!", stacktrace: str = ""):
        super().__init__(status_code=406, mensagem=mensagem, stacktrace=stacktrace)


class MensagemStatusCode(ApiClimaTempo):
    def __init__(self, status_code: int, mensagem: str, stacktrace: str = ""):
        super().__init__(status_code=status_code, mensagem=mensagem, stacktrace=stacktrace)


class RegistroJaInserido(ApiClimaTempo):
    def __init__(self, mensagem: str = "Registro já inserido!", stacktrace: str = ""):
        super().__init__(status_code=409, mensagem=mensagem, stacktrace=stacktrace)


class RegistroNaoEncontrado(ApiClimaTempo):
    def __init__(self, mensagem: str = "Registro não encontrado!", stacktrace: str = ""):
        super().__init__(status_code=404, mensagem=mensagem, stacktrace=stacktrace)


class Proibido(ApiClimaTempo):
    def __init__(self, mensagem: str = "Operação não permitida!", stacktrace: str = ""):
        super().__init__(status_code=403, mensagem=mensagem, stacktrace=stacktrace)


class Falha(ApiClimaTempo):
    def __init__(self, mensagem: str = "Operação não realizada!", stacktrace: str = ""):
        super().__init__(status_code=400, mensagem=mensagem, stacktrace=stacktrace)
