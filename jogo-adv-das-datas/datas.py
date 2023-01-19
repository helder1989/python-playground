
# arquivo com json pra armazenar a estrutura de um dicionário

import json
import random

f = open("word.json", encoding="utf8") # abrindo o arquivo json, usandi o utf8 para codificação de digitos

word = json.load(f)
choice_c = random.choice(list(word.keys())) # retornando todas as chaves do dicionário

print("Olá, seja bem vindo (a)!")
print("####################")

n_choices = 5 # o usuário terá 5 chances para advinhar a data
win = False # pra identificar se o usuário ganhou ou não


while n_choices > 0 and win is not True: # enquanto o usuário tiver alguma chance a lógica do jogo será repetida
    print("Dica: " + word[choice_c]) # fornecendo dicas para o usuário
    escolha_usuario = input("Data: DDMMAAAA\n")
    print("############# \n")

    # o usuário pode tentar trolar o programa, sendo assim vamos usar uma condicional
    if len(escolha_usuario)  != 8: # a função len vai nos dizer o tamanho dessa estrutura
        print("Erro na entrada. A resposta deve conter 8 digitos.")
        continue

    if escolha_usuario.isdigit(): # verificar se o que o usuário digitou é de fato um número
        check = []
        pontuacao = 0
        for i in range(8):
            if escolha_usuario[i] == choice_c[i]:
                check.append("V") # incrementando elementtos dentro desse estrutura
                pontuacao = pontuacao + 1
            else:
                check.append("F")

        print("Resposta: \n")
        print("|".join(check))
        print(" |".join(escolha_usuario))
        print("#########################\n")

        if pontuacao == 8:
            win = True

    else:
        print("Erro na entrada. A resposta deve ser uma data")
        continue
    n_choices = n_choices - 1

if win == True:
    print("Vitória!!!")
else:
    print("Derrota!!!")
    print(("A resposta era: " + choice_c))


# "V" quando o usuário acertar
# "F" quando o usuário errar
# | é pra definir a forma que os elementos devem ficar separados
# ######### pra ficar mais seperado, questão de origanização