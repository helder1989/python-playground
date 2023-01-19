from _datetime import datetime

def today(): # capturando o dia de hoje
    today = datetime.now()
    return today

# verificando o formato da data que o usuário registrou
def verify_date(date):
    try:
        date_format = datetime.strptime(date, "%d-%m-%Y")
        return date_format
    except:
        raise Exception("Entrada inválida! Formato sugerido: D-M-Y. Exemplo: 01-01-2023")
        # se tiver um erro vai encerrar a execução de tudo


def verify_due(date_ref):
    due_date = verify_date(date=date_ref)
    if today() > due_date: # verificando se a data de hoje é maior que a data que o usuário vai nos fornecer
        return "Data expirou..." # se isso acontecer é porque venceu
    else:
        return "Data não expirou..." # é porque não venceu


# nesse arquivo vamos realizar a lógica de verificar a data de hoje com a data de vencimento informada pelo usuário






