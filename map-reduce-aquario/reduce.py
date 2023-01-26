from functools import reduce

# o reduce está ligado a conta, somar, média ou algo assim

numbers = [1, 2, 3, 4, 5]

def sum(a, b):
    print("a = ", a) # trazendo o a e o b em cada interação
    print("b = ", b)
    print("a+b = " , a+b)
    return a+b
    # reduzindo a estrutura pra obter o resultado que queremos

print(reduce(sum,numbers))

# esse reduce.py foi para registrar os exemplos, o código será concentrado no mapreduce.py
