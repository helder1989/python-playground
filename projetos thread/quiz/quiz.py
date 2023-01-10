# mensagem que o usuário vai vê ao abrir, inicial
print("Seja bem vindo (a) ao Quiz do Helder!")

# temos que saber do usuário se ele deseja realizar o quiz

# tudo que o usuário digitar antes do enter será retornado nessa função
resposta_usuario = input("Deseja começar? (S/N) ")

# se o usuário digitar algo diferente de "S" temos que encerrar o programa, sendo assim vamos construir
# uma estrutura condicional
if resposta_usuario != "S":
    quit() # comando que vai encerrar o programa caso o usuário registre algo diferente de "S"
# caso a condição acima seja falsa o "quit" não será executado e vai seguir nas linhas de código que não fazem parte
# do if, ou seja, do mesmo nível de indentação

# criando um sistema de pontuação, a cada questão que o usuário acertar será atrubuído 1 ponto
score = 0

print("Iniciando...")
# começando as perguntas

# barra invertida (\) para quebra de linha
print("Quem foi o mito que desenvolveu o jogo Gran Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
resposta_1 = input("Resposta: ") # aguardando a resposta do usuário

if resposta_1 == "A": # verificando se o usuário respondeu corretamente
    print("Correto!") # informar ao usuário que ele acertou
    score = score + 1
else: # se não
    print("Incorreto!")

print("Qual o nome do protagonista do jogo GTA San Andreas? \n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Claudio Silva \n")
resposta_2 = input("Resposta: ")

if resposta_2 == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual é o nível máximo jogo GTA? \n (A) 299 \n (B) 499 \n (C) 999 \n (D) 199 \n")
resposta_3 = input("Resposta: ")

if resposta_3 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual é o objetivo do jogo GTA online)? \n (A) Acomular dinheiro \n (B) Comprar carros \n (C) comprar bens \n (D) Todas às alternativas \n")
resposta_4 = input("Resposta: ")

if resposta_4 == "D":
    print("Correto!")
    score = score + 1
else: # se não
    print("Incorreto!")

print(f"Quiz acabou... Pontuação: {score}/4")
# esse "f" identifica que o que vem dentro de aspas pode ser printado,lembrando que o /4 é referente
# a quantidade de perguntas


# sobre o sistema de pontuação se o usuário errar não será atribuido ponto negativo, somente vai deixar de ganhar mesmo


