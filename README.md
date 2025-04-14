# 🌍 Flask Geolocation App

Este é um aplicativo web simples desenvolvido com Flask. Ele permite ao usuário digitar um endereço e, ao enviar o formulário, retorna a latitude, longitude e o nome formatado do local, usando a API gratuita do Py4E (Python for Everybody).

## 🚀 Como funciona?

O app faz uma requisição à API de geolocalização `https://py4e-data.dr-chuck.net/opengeo?`, que retorna as coordenadas geográficas do endereço fornecido.

## 📦 Requisitos

- Python 3.6 ou superior
- Flask
- Acesso à internet

## 🔧 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/flask-geolocation-app.git
cd flask-geolocation-app

🗂 Estrutura
pgsql
Copiar
Editar
flask-geolocation-app/
├── app.py
├── templates/
│   └── index.html
├── README.md

🛠 Tecnologias utilizadas
Python

Flask

HTML (com Jinja2 para templates)

API Py4E OpenGeo

📃 Licença
Este projeto é de uso livre para fins educacionais.

Feito com 💻 + ☕ por [bugsenberg]