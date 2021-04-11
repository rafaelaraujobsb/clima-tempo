from enum import Enum
from typing import TypeVar

from bson import ObjectId
from pymongo import MongoClient
from pymongo.cursor import Cursor


ResultadoBuscaCollection = TypeVar('BuscaCollection', list, Cursor)


class TipoConexao(Enum):
    MONGODB = "mongodb"
    MONGODB_SRV = "mongodb+srv"


class ModMongo():
    """ Módulo mongo
    """
    def __init__(self, db: str, *, user: str = None, password: str = None, host: str = 'localhost', port: int = 27017,
                 tipo_con: TipoConexao = TipoConexao.MONGODB):
        """
        Faz a conexão com o db.
        """
        if user:
            if tipo_con == "mongodb":
                conexao = f'mongodb://{user}:{password}@{host}:{port}/{db}'
            else:
                conexao = f'mongodb+srv://{user}:{password}@{host}/{db}'
        else:
            conexao = f'mongodb://{host}:{port}/{db}'

        self.__client = MongoClient(conexao)
        self.__db = self.__client.get_database()

    def get_names_collections(self) -> list:
        """
        Busca todas as collections.

        :return: lista com o nome das collections.
        :rtype: list
        """
        return self.__db.collection_names()

    def build_index(self, collection: str, column: list, unique=False):
        """
        Cria um índice para a coleção.

        :param str collection: nome da collection
        :param str column: nome da chave que será usada como índice.
        :param str unique: True para chave indexada com valor único, senão False.
        """
        self.__db[collection].create_index(column, unique=unique)

    def index_info(self, collection: str):
        """
        Recupera o(s) índice(s) da collection.

        :returns: ndice(s) da collection.
        :rtype: dict
        """
        return self.__db[collection].index_information()

    def get_document(self, collection: str, filter: dict = None, visible: dict = None, max: int = 0,
                     sort: list = [('_id', 1)], cursor: bool = False) -> ResultadoBuscaCollection:
        """
        Busca todos os documentos encontrados.

        :param str collection: nome da collection
        :param dict filter: filtro da busca
        :param dict visible: colunas que serão mostradas ou não
        :param int max: quantidade máxima de matches
        :param list sort: | ordenação do resultado (ASCENDING = 1, DESCENDING = -1)
                          | Exemplo: [('_id', 1)]
        :param bool cursor: boleano para indicar se será retornado o cursor mongo

        :returns: resultado da busca
        :rtype: ResultadoBuscaCollection
        """

        resultado = self.__db[collection].find(filter, visible).sort(sort).limit(max)

        if not cursor:
            resultado = [r for r in resultado]

        return resultado

    def __next_id(self, collection: str) -> int:
        """
        Faz a geração de id para substir o objectid.

        :param str collection: nome da collection

        :returns: id sequencial gerado
        :rtype: int
        """

        resultado = self.__db.seqs.find_one_and_update({'_id': collection}, {'$inc': {'id': 1}}, upsert=True)

        if not resultado:
            _id = 1
        else:
            _id = resultado['id'] + 1

        return _id

    def set_document(self, collection: str, value: dict, auto: bool = False) -> ObjectId:
        """
        Insere um documento.

        :param str collection: nome da collection
        :param dict value: valor que será inserido
        :param bool auto: ativa o uso de ids

        :returns: id sequencial gerado
        :rtype: int

        .. note::
            Ao usar `auto` como True será usadao um int sequencial como _id.
        """
        if auto:
            value['_id'] = self.__next_id(collection)

        return self.__db[collection].insert_one(value).inserted_id

    def delete_document(self, collection: str, filter: dict) -> int:
        """
        Realiza a remoção de um documento específico no BD.

        :param str collection: nome da collection
        :param dict filter: filtro do documento

        :returns: Quantidade de documentos removidos
        :rtype: int
        """
        return self.__db[collection].delete_one(filter).deleted_count

    def update_document(self, collection: str, filter: dict, value: dict) -> int:
        """
        Altera um ou mais documentos.

        :param str collection: nome da collection
        :param dict filter: filtro da busca
        :param dict value: alteração a ser realizada

        :returns: quantidade de arquivos alterado
        :rtype: int

        .. note::
            `value` não precisa conter `$set`
        """

        if not any(map(value.get, ['$inc', '$set', '$push', '$pop'])):
            value = {'$set': value}

        result = self.__db[collection].update_many(filter, value)

        return result.modified_count

    def __enter__(self):
        """
        Abre a conexão com o gerenciador de contexto.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Encerra a conexão quando o objeto é destruído.
        """
        self.__client.close()
