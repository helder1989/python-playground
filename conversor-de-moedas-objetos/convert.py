
from requests import get

# requests é a biblioteca que será a ponte para que façamos as requisições
class convert_moedas:
    def __init__(self, api_key):
        self.url_base = "https://free.currconv.com"
        self.api_key = api_key # self se refere ao proprio objeto
        self.moedas = self.get_moedas()

    def get_moedas(self):
        endpoint = f"/api/v7/currencies?apiKey={self.api_key}"
        url = self.url_base + endpoint
        data = get(url).json()["results"]
        data = list(data.values())
        return data # retornar dados

    def show_moedas(self):
        for moeds in self.moedas:
            name = moeds.get("currencyName", "")
            _id = moeds.get("id", "")
            symbol = moeds.get("currencySymbol", "")
            print(f"{_id} | {name} | {symbol}")


    def transform_moedas(self, inicial_moeda, quantidade, final_moeda):
        endpoint = f"/api/v7/convert?q={inicial_moeda}_{final_moeda}"   # esse caso o usuário vai informar: A moeda inicial, a quantidade dessa moeda e moeda destino
        # que ele deseja
        parametros = ["&compact=ultra", f"&apikey={self.api_key}"] # lista com os parametros
        url = self.url_base + endpoint + "".join([str(parameter) for parameter in parametros])

        data = get(url).json()[f"{inicial_moeda}_{final_moeda}"]
        return data


# Uma api pode apresentar vários endpoint, e vamos utiliza-las conforme o nosso objetivo, interesse


