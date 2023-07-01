# Será uma API simples criada basicamente com duas linhas de código

from fastapi import FastAPI

app = FastAPI() # esse app é uma instãncia desse API

vendas = {     # criando dicionários
    1: {"Produto": "Lata de refrigerante", "preco_unitario": 6, "quantidade": 5},
    2: {"Produto": "Garrafa 2L", "preco_unitario": 20, "quantidade": 7},
    3: {"Produto": "Garrafa de vidro 800ml", "preco_unitario": 8, "quantidade": 10},
    4: {"Produto": "Mini lata", "preco_unitario": 2, "quantidade": 20},
    5: {"Produto": "Mini garrafa", "preco_unitario": 4, "quantidade": 50},
}

@app.get("/") # o link que o usuário vai acessar. Api está no ar dentro desse link
def home():  # defindo a função padrão, home page. Dentro dela vai ter tudo que quero que ela der como resposta
    return {"Vendas": len(vendas)} # um retorno do tamanho do dicionário "vendas"


@app.get("/vendas/{id_venda}") # contruindo uma nova rota aonde podemos pegar uma venda específica
def pegar_venda(id_venda: int):  # A função que vai rodar. int: definindo o tipo de varíavel
    if id_venda in vendas: # se o id_vendas estiver dentro do dicionário id_vendas
        return vendas[id_venda]
    else:    # senão
        return {"Erro": "ID da venda inválido"}




