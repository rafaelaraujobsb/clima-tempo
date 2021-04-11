from bson import ObjectId
from datetime import datetime

from scrapper_clima_tempo.config import envs
from scrapper_clima_tempo.modelos import tasks
from scrapper_clima_tempo.servicos.mod_database import ModMongo


class ConexaoClimaTempo(ModMongo):
    def __init__(self):
        super().__init__(envs.MONGO_DB, user=envs.MONGO_USR, password=envs.MONGO_PWD, host=envs.MONGO_HOST,
                         port=envs.MONGO_PORT, tipo_con=envs.MONGO_TIPO_CON)

    def _parser_colunas(self, *, resultado: list, parser: dict) -> list:
        resultado_parser = []
        for registro in resultado:
            resultado_parser.append({parser.get(chave, chave): str(valor) if isinstance(valor, ObjectId) else valor
                                     for chave, valor in registro.items()})

        return resultado_parser

    def criar_index(self, *, collection: str, indexes_collection: list):
        indexes = self.index_info(collection).keys()

        if len(indexes) - 1 < len(indexes_collection):
            for index in indexes_collection:
                self.build_index(collection=collection, column=index)

    def listar(self, *, collection: str, inicio: int, quantidade: int = 100, parser: dict = None, **kwargs) -> list:
        filtros = kwargs.get("filtros", {})
        resultado = self.get_document(collection, filter={"_id": {"$gte": inicio}, **filtros}, max=quantidade)

        if parser:
            resultado = self._parser_colunas(resultado=resultado, parser=parser)

        return resultado

    def buscar_anterior(self, *, collection: str, inicio: int, **kwargs) -> int:
        filtros = kwargs.get("filtros", {})
        resultado = self.get_document(collection, filter={"_id": {"$lt": inicio}, **filtros}, max=1)

        if resultado:
            id = resultado[0]["_id"]
        else:
            id = None

        return id


class CollectionAgendamento(ConexaoClimaTempo):
    COLLECTION = "agendamento"
    INDEXES = [[("data_inicio", 1), ("data_fim", 1)]]
    REGISTROS = [{"_id": "agendamento", "proxima_execucao": None, "intervalo": None}]

    def criar_index(self):
        super().criar_index(collection=CollectionAgendamento.COLLECTION,
                            indexes_collection=CollectionAgendamento.INDEXES)

    def carregar_base(self):
        for registro in CollectionAgendamento.REGISTROS:
            if not self.get_document(CollectionAgendamento.COLLECTION, filter={"_id": registro["_id"]}):
                self.set_document(CollectionAgendamento.COLLECTION, value=registro)

    def buscar(self) -> dict:
        resultado = self.get_document(CollectionAgendamento.COLLECTION, filter={"_id": "agendamento"})

        return resultado[0] if resultado else {}

    def atualizar(self, data: datetime, intervalo: int = 60) -> int:
        documento = {
            "proxima_execucao": data,
            "intervalo": intervalo,
        }

        return self.update_document(CollectionAgendamento.COLLECTION, filter={"_id": "agendamento"}, value=documento)


class CollectionTempos(ConexaoClimaTempo):
    COLLECTION = "tempos"
    INDEXES = [[("estado", 1)], [("municipio", 1)], [("data_cadastro", -1)]]
    PARSER = {"_id": "id_tempo"}

    def criar_index(self):
        super().criar_index(collection=CollectionTempos.COLLECTION, indexes_collection=CollectionTempos.INDEXES)

    def cadastar(self, *, estado: str, municipio: str, umidade: str, pressao: str, vento: str, temperatura: str) -> int:
        documento = {
            "estado": estado,
            "municipio": municipio,
            "tempo": {
                "umidade": umidade,
                "pressao": pressao,
                "vento": vento,
                "temperatura": temperatura,
            },
            "data_cadastro": datetime.now()
        }

        return self.set_document(CollectionTempos.COLLECTION, value=documento, auto=True)


class CollectionExecucoes(ConexaoClimaTempo):
    COLLECTION = "execucoes"
    INDEXES = [[("estado", 1)], [("municipio", 1)], [("data_inicio", -1), ("data_fim", -1)]]
    PARSER = {"_id": "id_execucao"}

    def criar_index(self):
        super().criar_index(collection=CollectionExecucoes.COLLECTION, indexes_collection=CollectionExecucoes.INDEXES)

    def cadastar(self, *, estado: str, municipio: str) -> int:
        documento = {
            "estado": estado,
            "municipio": municipio,
            "data_inicio": datetime.now(),
            "data_fim": None,
            "status": tasks.Status.EM_EXECUCAO.value,
            "erro": None
        }

        return self.set_document(CollectionExecucoes.COLLECTION, value=documento, auto=True)

    def atualizar(self, id_execucao: int, *, erro: dict = None) -> int:
        documento = {
            "data_fim": datetime.now(),
            "status": tasks.Status.ERRO.value if erro else tasks.Status.FINALIZADO.value,
            "erro": erro
        }

        return self.update_document(CollectionExecucoes.COLLECTION,
                                    filter={"_id": id_execucao}, value={"$set": documento})


class CollectionMunicipios(ConexaoClimaTempo):
    COLLECTION = "municipios"
    INDEXES = [[("estado", 1), ("municipio", 1)]]
    PARSER = {"_id": "id_municipio"}

    def criar_index(self):
        super().criar_index(collection=CollectionMunicipios.COLLECTION, indexes_collection=CollectionMunicipios.INDEXES)

    def listar_cursor(self) -> list:
        yield from self.get_document(CollectionMunicipios.COLLECTION, cursor=True)
