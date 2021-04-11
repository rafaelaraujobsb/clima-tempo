<div align="center"><h1>Projeto Scrapper Clima Tempo</h1></div>

## ✒️ Introdução
O projeto tem como objetivo extrair dados do site [Tempo Agora](https://www.tempoagora.com.br/) e disponibilizar informações sobre a extração através de uma API.
Para mais detalhes de cada serviços acesse os links abaixo:
- [API](./api)
- [Scrapper](./scrapper)

## 🔌 Instalação da Aplicação
```
docker-compose -f docker-compose.dev.yaml build --no-cache
```

## ⚙️ Variáveis de ambiente
Acesse o README de cada serviço para verificar quais as variáveis são necessárias.
- [API](./api)
- [Scrapper](./scrapper)


## 📀 Iniciar Aplicação
```
docker-compose -f docker-compose.dev.yaml up
```

Após a inicialização dos containers os seguinte serviços poderão ser acessados:
- [API](http://localhost:9080/swagger)
- [RabbitMQ](http://localhost:8080)
    - `climatempo` é a senha e usuário

## 🧔 Responsável pelo projeto
<p><a href="mailto:bsb.rafaelaraujo@gmail.com.br">Rafael Araujo</a></p>
<div align="center"><img width="500" alt="Logo" src="https://s3.amazonaws.com/sample-login/companies/avatars/000/003/383/original/gaivota_logo_oficial.png?1541450807"></div>