import re
import unicodedata
from datetime import datetime
from json import loads

from loguru import logger
from requests import Request, Session

from scrapper_clima_tempo.config import envs
from scrapper_clima_tempo.exceptions import Falha


RE_NUXT_CLIMA = re.compile(r"window\.__NUXT__=(.*)(?=;<\/script>)")


class ScrapperClimaTempo:
    def __init__(self):
        self.__sessao = Session()
        self.__sessao.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        }
        self.campos = [("temp", "temperatura"), ("wind", "vento"), ("pressure", "pressao"), ("humidity", "umidade")]

    def __requisicao(self, endpoint: str) -> dict:
        req = Request(method="GET", url=f"{envs.URL_CLIMATEMPO}{endpoint}").prepare()

        logger.info(f"[+] REQUISITANDO {req.url}")
        t_inicio = datetime.now()
        requisicao = self.__sessao.send(req)
        logger.info(f"[+] TEMPO REQUISICAO {req.url} {datetime.now() - t_inicio}")

        if requisicao.status_code == 200:
            if nuxt_clima := RE_NUXT_CLIMA.search(requisicao.text):
                json = loads(nuxt_clima.group(1))
            else:
                logger.error("[-] __NUXT__ NÃO ENCONTRADO")
                raise Falha(mensagem="Não foi encontrado o __NUXT__ na página!", stacktrace=requisicao.text)
        else:
            logger.error(f"[-] PROBLEMA COM A REQUISIÇÃO {requisicao.url}")
            raise Falha(mensagem="Ocorreu um problema com a requisição!", stacktrace=requisicao.text)

        return json

    def buscar_clima(self, *, estado: str, municipio: str) -> dict:
        municipio = unicodedata.normalize('NFKD', municipio.lower().replace(" ", "")).encode('ascii', 'ignore').decode()
        resultado = self.__requisicao(f"/{estado}/{municipio}")

        return {parse: resultado["state"]["weatherCityData"][campo] for campo, parse in self.campos}
