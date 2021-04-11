class ScrapperClimaTempo(Exception):
    """ Classe Base """

    def __init__(self, status_code: int, mensagem: str, stacktrace: str = ""):
        self.mensagem = mensagem
        self.stacktrace = stacktrace
        self.status_code = status_code

    def __repr__(self):
        return f"\n---> Status: {self.status}\n---> Mensagem: {self.mensagem}\n---> Stacktrace: {self.stacktrace}"

    def __str__(self):
        return self.mensagem


class Falha(ScrapperClimaTempo):
    def __init__(self, mensagem: str = "Operação não realizada!", stacktrace: str = ""):
        super().__init__(status_code=400, mensagem=mensagem, stacktrace=stacktrace)
