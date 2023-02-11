# a api é um dado sensível, pois se a gente for pagar por ela no caso, se for gratuita que é o nosso
# caso está tudo bem. Já é projetos comerciais não é bom expor a api

# A API Key é pessoa e deve ser solicitada no site da Api, e vamos recebe-lá via e-mail

from convert import convert_moedas

# importando a classe, ou seja, todos os metódos atrelhados a ela

api_key = "ac9e5dd2642cad6906b6"
conv_moed = convert_moedas(api_key)
print(conv_moed.transform_moedas("BRL", 20, "USD"))
