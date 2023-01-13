
# o usuário vai nos fornecer um número por exemplo 10 e o algorítimo vai gerar um número entre 0 e 10
# em seguida o usuário terá que acertar qual número o algorítimo gerou

# biblioteca para geradores de números em várias distribuições
import random

print("Seja bem vindo (a) ao Questionário do Helder!")
escolha_numero = input("Registre o número teto do desafio: ")

# verifica se o que esá dentro da variavel escolha_numero é de fato é um número
if escolha_numero.isdigit():
    escolha_numero = int(escolha_numero)
else:
    print("Erro: valor informado não é númerico. Gentileza execute novamente e registre um número!")
    quit()
random_numero = random.randint(0, escolha_numero) # estamos gerando um número randomico

n_tentativas = 0 # quantas vezes o usuário demorou para aadvinhar o número

while True: # enquanto
    resposta_usuario = input("Advinhe o número: ")

    if resposta_usuario.isdigit():
        resposta_usuario = int(resposta_usuario)
    else:
        print("Erro: valor informado não é númerico: Gentileza informe um número!") # quando o usuário inserir algo
            # diferente de número
        continue # vai ingnorar o que está abaixo e repetir o ciclo desde o começo

    n_tentativas = n_tentativas + 1
    if resposta_usuario == random_numero: # verificando se o número que o usuário registrou é igual ao
    # número gerado
        print("Acertou!")
        break # vai quebrar o ciclo "infinito", pois o ciclo é infinito enquanto o usuário não acertar
    elif resposta_usuario > random_numero:   # vamos incrementar opções, condições
        print("Chutou alto, pois o número randomico é menor que isso...")
    else:
        print("Chutou baixo, pois o número randomico é maior que isso...")
# chutou alto ou baixo tem o objetivo de ajudar o usuário à advinhar

print("N° de tentativas: " + str(n_tentativas)) # será feito uma concatenação
# ao final será informado o número de tentativas que o usuário realizou até advinhar









