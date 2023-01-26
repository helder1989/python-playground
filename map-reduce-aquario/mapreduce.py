import json
from functools import reduce

f = open("../filtrando-map-animais-aquario/aquario.json", encoding="utf8")
data_aquario = json.load(f)
animais = data_aquario["data"]

# só queremos a informação "tipo dos animais
def pick_animal_type(animal):
    return animal["type"], 1

def reducer(acc, val): # variável acumuladora e variável padrão
    if val[0] not in acc.keys(): # verificando se o val[0} está dentro do meu dicionário
        acc[val[0]] = 0 + val[1]
    else:
        acc[val[0]] = acc[val[0]] + val[1]
    return acc # acc é o acumulador

type_animais = list(map(pick_animal_type, animais))
print(type_animais) # vai trazer uma estrutura de tupla, começa com () e encerra com ()
animais_type_count = reduce(reducer, type_animais, {})
print(animais_type_count) # contando os tipos de animais do nosso aquário, json

# no final vamos ter um dicionário

