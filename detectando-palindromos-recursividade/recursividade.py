# a função a ser construída deverá detectar se uma determinada palavrar é palindroma
# ou seja é uma palavra que tem o mesmo sentido sendo lida de frente pra trás e de trás pra frente

# verificando se uma palavra é palindroma ou não: a ordem das letras da palavra devem ser a
# mesma no sentido normal e no sentido contrário, tendo essas igualdades temos uma palavra palindroma

import math
# funções matemáticas

def is_palindrome(word):
    j = len(word)-1
    result = 0
    for i in range(len(word)): # do tamanho da palavra
        if word[i] == word[j]: # verificando se a primeira letra é igual a última
            result = result + 1
        if i >= j: # quando o i encontrar com o j vamos quebrar o ciclo
            break
        j = j - 1
    if result == math.ceil(len(word)/2): # se der um valor quebrado a função ceil vai arrendodar pra cima
        return True # se isso acontecer vamos ter o retorno verdadeiro
    else:
        return False # se isso não acontecer vamos ter o retorno de falso

    def is_palindrome_recursive(word): # a função vai chamar ela própria
        if len(word) <= 1: # verificando se o tamanho da palavra é menor ou igual a 1
            return True
        else:
            return word[0] == word[-1] and is_palindrome_recursive(word[1:-1])
            # indo na lógica ao contrário


words = ["arara", "raceca", "carro", "cama", "level"]

for word in words:
    print(word)
    print(is_palindrome(word))
    print("\n") # quebra de linha

