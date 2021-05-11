<div align="center"><h1>API Clima Tempo</h1></div>


## ✒️ Introdução
API para expor os dados gerados pelo [scrapper](../scrapper).

## 🔌 Instalação da Aplicação
### Imagem Docker
docker build -t api_clima_tempo:0.4.0 .

### Pacote Python
pip install .

## ⚙️ Variáveis de ambiente
| Nome | Descrição | Default |
|-|-|-|
|MONGO_USR|Usuário do banco de dados|N/A|
|MONGO_PWD|Senha do banco de dados|N/A|
|MONGO_HOST|Host do banco de dados|N/A|
|MONGO_DB|Nome do banco de dados|climatempo|
|MONGO_PORT|Porta do banco de dados|27017|
|MONGO_TIPO_CON|Tipo da conexão com o banco de dados (mongodb e mongodb+srv)|mongodb|

## 📀 Iniciar Aplicação
Antes de inicializar a aplicação export as variáveis de ambiente na máquina.
```shell
export NOME_ENV=123
```

### Docker
```shell
docker run --name api_climatempo -p 9080:8080 -e MONGO_USR=$MONGO_USR -e MONGO_PWD=$MONGO_PWD -e MONGO_HOST=$MONGO_HOST -e MONGO_PORT=$MONGO_PORT api_clima_tempo:0.4.0 
```

### Local
```shell
gunicorn -w 3 -b :9080 -k uvicorn.workers.UvicornWorker -t 90 --preload --max-requests=500 api_clima_tempo:app
```


## 🛠️ Ferramentas Utilizadas
<a href="https://docs.python.org/3.8/">Python3.8</a><br>
<a href="https://fastapi.tiangolo.com/">FastAPI</a><br>
<a href="https://pymongo.readthedocs.io/en/stable/index.html">PyMongo</a><br>
<a href="https://github.com/Delgan/loguru">Loguru</a><br>
<a href="https://pylama.readthedocs.io/en/latest/">Pylama</a><br>

## 🧔 Responsáveis pelo projeto
<p><a href="mailto:bsb.rafaelaraujo@gmail.com.br">Rafael Araujo</a></p>
