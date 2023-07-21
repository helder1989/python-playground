
# Interação com o usuário

nota1 = int(input("Insira uma nota:  "))
nota2 = int(input("Registre outra nota: "))

# Calculando a soma das duas notas

soma = nota1+nota2

# Calculo da média entre as duas notas

media = soma / 2

print("A média entre as duas notas é:", media)

if media >=25:
    print("Parabéns, você foi aprovado!!!")

else:
    print("Que pena, se esforce mais!!!")

