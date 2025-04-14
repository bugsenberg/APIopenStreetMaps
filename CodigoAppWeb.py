from flask import Flask, request, render_template
import urllib.request, urllib.parse
import json, ssl

app = Flask(__name__)

# Função para obter as coordenadas (latitude e longitude) a partir do endereço fornecido
def get_coordinates(address):
    ServiceUrl = 'https://py4e-data.dr-chuck.net/opengeo?'

    # Ignora erros de certificado SSL
    Ctx = ssl.create_default_context()
    Ctx.check_hostname = False
    Ctx.verify_mode = ssl.CERT_NONE

    # Codifica o endereço na URL
    Address = address.strip()
    Parms = dict()
    Parms['q'] = Address
    Url = ServiceUrl + urllib.parse.urlencode(Parms)

    # Faz a requisição e lê os dados
    try:
        Uh = urllib.request.urlopen(Url, context=Ctx)
        Data = Uh.read().decode()
        Js = json.loads(Data)

        # Verifica se o resultado contém dados e retorna as coordenadas
        if not Js or 'features' not in Js or len(Js['features']) == 0:
            print("Erro: Localização não encontrada.")
            return None, None, "Localização não encontrada"

        lat = Js['features'][0]['properties']['lat']
        lon = Js['features'][0]['properties']['lon']
        location = Js['features'][0]['properties']['formatted']

        return lat, lon, location
    except Exception as e:
        print(f"Erro ao consultar a API: {e}")
        return None, None, "Erro ao consultar a API"

# Rota principal da aplicação
@app.route('/', methods=['GET', 'POST'])
def home():
    lat = lon = location = error = None

    # Processa o formulário
    if request.method == 'POST':
        address = request.form['location']
        print(f"Endereço recebido: {address}")  # Depuração

        lat, lon, location = get_coordinates(address)
        print(f"Latitude: {lat}, Longitude: {lon}, Localização: {location}")  # Depuração

        if lat is None or lon is None:
            error = location  # Em caso de erro, exibe a mensagem da API
            print(f"Erro na consulta: {error}")  # Depuração

    return render_template('index.html', lat=lat, lon=lon, location=location, error=error)

if __name__ == "__main__":
    app.run(debug=True)
