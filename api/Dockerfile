FROM python:3.9-alpine3.13

RUN apk add --no-cache alpine-sdk tzdata
ENV TZ=America/Sao_Paulo

COPY README.md setup.py /deploy/
COPY api_clima_tempo /deploy/api_clima_tempo

VOLUME [ "/deploy" ]

WORKDIR /deploy

RUN pip3 install .

EXPOSE 8080
CMD ["gunicorn", "-w", "3", "-b", ":8080", "-k", "uvicorn.workers.UvicornWorker", "-t", "90", \
     "--preload", "--max-requests=500", "api_clima_tempo:app"]