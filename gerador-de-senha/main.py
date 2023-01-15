
import random
import string

# criando uma função
def senha_gerador(len_pass = 8):
    ascii_opcoes = string.ascii_letters
    numero_opcoes = string.digits
    pontape_opcpes = string.punctuation
    opçoes = ascii_opcoes + numero_opcoes + pontape_opcpes # concatenação

    senha_usuario = ""

    for i in range(0, len_pass): # o range vai criar uma estrutura de lista. o i é uma variavél auxiliar pra viabilizar a quantidade de repetição
        digit = random.choice(opçoes)
        senha_usuario = senha_usuario + digit # concatenação

    return senha_usuario

escolha_usuario = input("Quantos digitos na senha?")

if escolha_usuario.isdigit():
    escolha_usuario = int(escolha_usuario)

else:
    print("Entrada inválida!")
    quit()

resposta = senha_gerador(len_pass = escolha_usuario)
print(f"Senha gerada:\n{resposta}")







        










