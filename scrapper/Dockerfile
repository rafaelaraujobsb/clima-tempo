FROM python:3.9-slim

ENV TZ=America/Sao_Paulo

ENV BROKER \
    MONGO_USR \
    MONGO_PWD \
    MONGO_HOST \
    MONGO_DB="climatempo" \
    MONGO_PORT="27017" \
    MONGO_TIPO_CON="mongodb" \
    TS_SCHEDULE="1" \
    URL_CLIMATEMPO="https://www.tempoagora.com.br/previsao-do-tempo"

COPY README.md setup.py /deploy/
COPY scrapper_clima_tempo /deploy/scrapper_clima_tempo

VOLUME [ "/deploy" ]

WORKDIR /deploy

RUN pip3 install .

CMD ["sh"]