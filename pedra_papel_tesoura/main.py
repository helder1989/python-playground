
import random

# variavéis com a armazeando a pontuação do usuário e do cumputador
pontos_usuario = 0
pontos_computador = 0

opcoes = ["r", "t", "p"] # lista

while True: # enquanto a condição que estiver dentro do while for verdadeira o ciclo segue rodando
    escolha_usuario = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair.").lower()
# o lower é para fazer tipo um combo de funções, executando tudo que vem antes dele, retornando tudo em minusculo

    if escolha_usuario == 'q': # caso o usuário registre o "q" vamos fazer a quebra do cliclo
        break

    # verificando se o que o usuário digitou não está dentro da variável opcoes
    if escolha_usuario not in opcoes:
        continue

    escolha_cumputador = random.randint(0, 2) # momento em que o cumputador fará a escolha, pedra, papel
    # ou tesoura a idéia é 0: R, 1 : T, 2: P
    opcao_cumputador = opcoes[escolha_cumputador]

    print(" O cumputador escolheu " + opcao_cumputador)

    if escolha_usuario == opcao_cumputador:
        print("Empate!")
    elif escolha_usuario == "r" and opcao_cumputador == "t":
        print("Você ganhou!")
        pontos_usuario = pontos_usuario + 1

    elif escolha_usuario == "p" and opcao_cumputador == "r":
        print("Você ganhou!")
        pontos_usuario = pontos_usuario + 1

    elif escolha_usuario == "t" and opcao_cumputador == "p":
        print("Você ganhou!")
        pontos_usuario = pontos_usuario + 1

    # não empatou e o usuário não ganhou em nenhuma das condições acima o que resta é o cumputador ganhar
    else:
        print("Você perdeu!")
        pontos_computador = pontos_computador + 1
print("Sua pontuação:" + str(pontos_usuario))
print("Pontuação do Computador: " + str(pontos_computador))

if pontos_computador > pontos_usuario:
    print("Derrota!!!!!")
elif pontos_computador == pontos_usuario:
    print("Empate")
else:
    print("Vitória!!")

print("Até logo!")






