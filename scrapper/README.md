<div align="center"><h1>Scrapper Clima Tempo</h1></div>


## ✒️ Introdução
O projeto foi desenvolvido utilizando Celery com RabbitMQ para gerenciar as tarefas de extração de dados do site [Tempo Agora](https://www.tempoagora.com.br/)

### Serviços:
**Beat:** responsável por adicionar mensagens na fila do worker que verifica os agendamentos

**Worker Verificar Agendamento:** responsável por verificar se já está na hora de executar o scrapper dos municípios

**Worker Scrapper:** responsável por realizar o scrapper e capturar os dados do tempo de cada município

## 🔌 Instalação da Aplicação
### Imagem Docker
docker build -t scrapper_clima_tempo:0.3.0 .

### Pacote Python
pip install .

## ⚙️ Variáveis de ambiente
| Nome | Descrição | Default |
|-|-|-|
|BROKER|Dados de conexão com o RabbitMQ (amqp://usuario:senha@host:porta/)|N/A|
|MONGO_USR|Usuário do banco de dados|N/A|
|MONGO_PWD|Senha do banco de dados|N/A|
|MONGO_HOST|Host do banco de dados|N/A|
|MONGO_DB|Nome do banco de dados|climatempo|
|MONGO_PORT|Porta do banco de dados|27017|
|MONGO_TIPO_CON|Tipo da conexão com o banco de dados (mongodb e mongodb+srv)|mongodb|
|TS_SCHEDULE|Intervalo em minutos da verificação do agendamento|1|
|URL_CLIMATEMPO|URL do site Clima Agora|https://www.tempoagora.com.br/previsao-do-tempo|

## 📀 Iniciar Aplicação
Antes de inicializar a aplicação export as variáveis de ambiente na máquina.
```shell
export NOME_ENV=123
```

### Celery Beat
```shell
celery -A scrapper_clima_tempo beat --loglevel=INFO
```
#### Docker
```shell
docker run --name beat_climatempo -e MONGO_USR=$MONGO_USR -e MONGO_PWD=$MONGO_PWD -e MONGO_HOST=$MONGO_HOST -e MONGO_PORT=$MONGO_PORT -e BROKER=$BROKER scrapper_clima_tempo:0.3.0 celery -A scrapper_clima_tempo beat --loglevel=INFO
```

### Worker Verificar Agendamento
```shell
celery -A scrapper_clima_tempo worker --concurrency=1 --loglevel=INFO -n scheduler@%h -Q climatempo_scheduler
```
#### Docker
```shell
docker run --name agendamento_climatempo -e MONGO_USR=$MONGO_USR -e MONGO_PWD=$MONGO_PWD -e MONGO_HOST=$MONGO_HOST -e MONGO_PORT=$MONGO_PORT -e BROKER=$BROKER scrapper_clima_tempo:0.3.0 celery -A scrapper_clima_tempo worker --concurrency=1 --loglevel=INFO -n scheduler@%h -Q climatempo_scheduler
```

### Worker Scrapper
```shell
celery -A scrapper_clima_tempo worker --concurrency=8 --loglevel=INFO -n scrapper@%h -Q climatempo_buscar_clima
```
#### Docker
```shell
docker run --name scrapper_climatempo -e MONGO_USR=$MONGO_USR -e MONGO_PWD=$MONGO_PWD -e MONGO_HOST=$MONGO_HOST -e MONGO_PORT=$MONGO_PORT -e BROKER=$BROKER scrapper_clima_tempo:0.3.0 celery -A scrapper_clima_tempo worker --concurrency=8 --loglevel=INFO -n scrapper@%h -Q climatempo_buscar_clima
```

## 🛠️ Ferramentas Utilizadas
<a href="https://docs.python.org/3.8/">Python3.8</a><br>
<a href="https://docs.celeryproject.org/en/stable/index.html">Celery</a><br>
<a href="https://2.python-requests.org/en/master/">Requests</a><br>
<a href="https://pymongo.readthedocs.io/en/stable/index.html">PyMongo</a><br>
<a href="https://github.com/Delgan/loguru">Loguru</a><br>
<a href="https://pylama.readthedocs.io/en/latest/">Pylama</a><br>

## 🧔 Responsáveis pelo projeto
<p><a href="mailto:bsb.rafaelaraujo@gmail.com.br">Rafael Araujo</a></p>
<div align="center"><img width="500" alt="Logo" src="https://s3.amazonaws.com/sample-login/companies/avatars/000/003/383/original/gaivota_logo_oficial.png?1541450807"></div>