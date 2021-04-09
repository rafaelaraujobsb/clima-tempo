def parse_openapi(respostas: dict) -> dict:
    return {status: {"content": {"application/json": {"example": resposta.dict()}}, "model": resposta.__class__}
            for status, resposta in respostas.items()}
