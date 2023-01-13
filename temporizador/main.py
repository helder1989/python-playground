
import time

t = input("Digite o tempo (em segundos): ") # aguardando o usuário digitar

if t.isdigit():
    t = int(t)
else:
    print("Entrada inválida!")
    quit()
# 120 / 60 = 2
# 150 / 60 = 2 | 30

# divmod retorna um par de números que consiste em seu quociente e restante ao usar a divisão inteira

while t: # enquanto a condição for verdadeira a execução segue, se for falso vai encerrar a execução
    minutos, segundos = divmod(t, 60)
    cronometro = "{:02d}:{:02d}".format(minutos, segundos)
    print(cronometro, end="\r")
    time.sleep(1) # entre um print e outro vamos conceder 1 segundo de descanso,ficando melhor para o usuário visualizar
    t = t - 1

print("O tempo finalizou!!!")

# print(cronometro, end="\r") # a redução do tempo será mostrada na mesma linha de código
# format é uma outra forma de colocar a variável dentro da str, onde tiver {} será acrescentado as nossas
# variáveis registrando dentro dos {} o formato de str que queremos exibir
