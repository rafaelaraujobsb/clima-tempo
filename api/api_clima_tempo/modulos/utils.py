def parse_openapi(respostas: dict) -> dict:
    return {status: {"content": {"application/json": {"example": resposta.dict()}}, "model": resposta.__class__}
            for status, resposta in respostas.items()}


def montar_paginacao(*, resultado: list, anterior: int, quantidade: int, chave_proximo: str = None) -> dict:
    if len(resultado) == quantidade + 1:
        proximo = resultado.pop()[chave_proximo]
    else:
        proximo = None

    return {"anterior": anterior, "proximo": proximo}
