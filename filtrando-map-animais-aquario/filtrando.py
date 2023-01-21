
# Colocar todos os animais do tipo Fish no tanque de número 42

import json

f = open("aquario.json", encoding="utf8")
data_aquarium = json.load(f) # carregando um dicionário a partir de um arquivo json
animals = data_aquarium["data"]

def verify_fish(animal):
    if animal["type"] == "fish":
        return True
    return False

animals_fish = list(filter(verify_fish, animals)) # o filter "filtro" terá um papel interativo

def animal_name(animal):
    return animal["name"]

animals_fish_name = list(map(animal_name, animals_fish))
print(animals_fish_name)

def assign_to_tank(animals, names_selected, new_tank_number): # inserindo os animais do tipo fish no tanque 42
    def chance_tank_number(animal):
        if animal["name"] in names_selected:
            animal["tank number"] = new_tank_number
            return animal
    return list(map(chance_tank_number, animals))

new_aquario = assign_to_tank(animals, animals_fish_name, 42)
print(new_aquario)

# nesse bloco de código foi definido função dentro de outra função


# animals_fish = list(filter(lambda animal: (animal["type"] == "fish"), animals))
# vai da true ou false no final

# função lambda: funções que o usuário não precisa definir, ou seja, não vai precisar escrever a função e
# depois utilizá-la dentro do código. É uma forma de deixar o nosso código mais limpo também


# formato json, o valor dessa chave [] no arquivo aquario.json é uma lista e cada elemento da lista é um dicionário

# O map vai aplicar uma função em cada item de uma lista de itens, ou seja, é um for com uma chamada da função para
# aplicá-la a cada item da sua lista