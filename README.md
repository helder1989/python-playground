### Quiz em Python
Esse projeto visa construir um quiz no qual vamos registrar perguntas, respostas e pontuação.

Por conta própria acrescentei mais duas questões.

A pontuação máxima vai de acordo com a quantidade de questões e o ponto atribuído a cada uma delas, no caso desse experimento a cada questão foi atribuída o valor de 1 ponto.

### Construindo Jogo de Adivinhação Numérica em Python

O objetivo é elaborar um projeto de jogo de adivinhação numérica. O usuário irá dizer um número. O programa irá gerar um número aleatório entre 0 e o número digitado pelo usuário. O programa irá dar dicas pro usuário para auxiliar ele chegar mais perto do número gerado pelo programa. No fim, ao acertar, o programa irá informar a quantidade de negociações efetuadas até acertar o número.

### Pedra, papel e tesoura em Python 

Nesse projeto o usuário vai escolher um dos três: pedra, papel ou tesouro e a nossa máquina, cumputador vai realizar uma escolha também e teremos a contagem de quem ganhou. E no fim teremos o resultado. 


### Temporizador em Python

Nesse projeto vamos construir uma aplicação que simula um temporizador. O usuário digita o tempo desejado em segundos, logo em seguida no terminal é exibido o temporizador reduzindo o tempo no formato "minutos:segundos" até atingir "00:00" e assim encerrar a execução da aplicação. Vamos lidar com outra forma de inserir variáveis dentro da string, além de aprofundar os conhecimentos no que tange nas funções do Python. 


### Gerador automático de senha

A ideia nesse experimento é que quando o usuário chamar o programa e o programa perguntar quantos digitos queremos nessa senha o porograma mesmo vai gerar de forma aleatória da forma que o usuário solicitou. E para cada dígito da senha o programa mesmo vai escolhendo cada um de maneira aleátoria, letras, números e caracteres especiais. 

### Jogo de advinhação de datas

Nesse experimento construímos um jogo de adivinhação envolvendo datas históricas, inspirado no termoo, em Python. Neste projeto lidamos com estrutura de dicionário, arquivos JSON, algumas funções envolvendo estrutura de listas e manipulando variáveis boleanas. A inpiração para o nosso projeto será o jogo TERMO https://term.ooo/ o game nada mais é que um tipo de joguinho da forca no qual não há dicas, além das cores dos quadrados. Em nosso caso o usuário terá que advinhar a data (DD/MM/AAAA) e quando o jogo for iniciado o usuário receberá um dica sobre um acontecimento na data, sendo assim através da dica ele seguirá escolhendo a data. O nosso programa vai escolher uma data de forma aleatória e o usuário será informado sobre qual digíto ele acertou, qual errou. 

### Datas e Funções

Nesse projeto a ideia é verificar se um determinado produto venceu, aplicando funções no geral. O nosso programa vai perguntar para o usuário qual é a data de vencimento e vamos comparar as datas, a data informada com a data atual.

### Detectando palindromos com recursividade

#### O que é palíndromo?

O termo palíndromo vem do grego palin, “de novo”, e dromo, “percurso”, “circuito”, ou seja, um caminho percorrido novamente. Assim como outros elementos da língua portuguesa, os palíndromos podem ser utilizados por escritores e redatores talentosos para causar determinadas sensações no leitor.

**Recursividade** é o mecanismo de programação no qual uma definição de função ou de outro objeto refere-se ao próprio objeto sendo definido. Assim função recursiva é uma função que é definida em termos de si mesma. Recursividade é o mecanismo básico para repetições nas linguagens funcionais. **A recursidade não é exclusiva do python, ou seja, pode-se encontrada em outras linguagens de programação.**

### Filtrando e Mapeando Animais de um Aquário

O objetivo nesse experimento é fazer um desafio em cima de um JSON de dados de animais de um aquário. Sendo assim vamos transferir os animais do tipo FISH para o tanque 43. Isso será feito utilizando as estruturas filter e map do Python, evitando o uso de estruturas de repetição como "while" e "for", pois a ideia é deixar o cógigo ainda mais limpo e compreensível. Nesse desafio também vamos fazer o uso da lambda no lugar das funções dwfinidas como conhecemos.


### Coletando e exibindo Dados do NBA com API

Nesse projeto o objetivo é realizar a coleta de dados envolvendo jogos e times do NBA, utilizando uma conceito de API. Realizando a extração dos dados, aplicando alguns tratamentos para melhorar a exibição desses dados ao usuário. 

#### O que seria uma API?

APIs são mecanismos que permitem que dois componentes de software se comuniquem usando um conjunto de definições e protocolos. Muitas empresas, utilizam as APIs para facilitar a obtenção ou troca de informações. Quando vamos realizar login ou nos cadastrar em algum site, a página de acesso pode utilizar-se das nossas contas já salvas no servidor para obter nossos dados e assim para concluir o login/cadastro no site, por exemplo. Quando isso acontece é uma API disponibilizando opção de logar com sua conta do Facebook ou e-mail já existentes ali. A grosso modo API é como se fosse um "garçom", pois nos clientes não temos acesso à cozinha, sendo o garçom (API) o facilitador. Esse é o link do site no qual faremos a requisição dos dados: http://data.nba.net/prod/v1/today.json que é composto por uma estrutura de dicionário que também nos concede alguns links que permite acesso à vários dados da NBA. Por exemplo, podemos acessar o link mencionado e copiar e colar o link referente ao dados que precisamos e mudar a URL > http://data.nba.net/prod/v1/today.json **para** http://data.nba.net/**prod/v1/allstar/2018/AS_roster.json** adcionando o link após a palavrar "net/". Dentro desse contexto devemos ir entendendo a estrutura do json, raramente à API vai trazer os dados prontos para serem consumidos, ou seja, vamos aplicar o processo de **ETL**, extrair os dados de através de uma API, trasformar os dados se adptando ao jeito que precisamos e por último carregamos esses dados em algum local, pode ser em um banco de dados, excel e etc. 

#### O que NBA?

NBA é uma abreviação para National Basketball Association, que traduzido para português significa: Associação Nacional de Basquetebol. Em suma, essa é a maior liga de basquete do Mundo. Sendo considerada por muitos, a maior e melhor liga do mundo. Participam deste campeonato, ao todo, 30 times de basquetebol. Sendo que 29 são dos Estados Unidos e 1 do Canadá.


### Extraindo dados do Airbnb (Em andamento)

A ideia nesse experimento é construir um estudo de web scraping utilizando a biblioteca BeautifulSoup, em que vamos extrair dados dos iomóveis da página de busca. 

A coleta de dados web, ou raspagem web, é uma forma de mineração que permite a extração de dados de sites da web convertendo-os em informação estruturada para posterior análise. O tipo mais básico de coleta é o download manual das páginas, copiando e colando o conteúdo, e isso pode ser feito por qualquer pessoa, sendo esse o processo de web scraping.

O Airbnd é uma plataforma de aluguel de hospedagens, que permite que qualquer pessoa disponibilize ou reserve acomodações ao redor do mundo. Seu grande diferencial é oferecer alternativas às hospedagens tradicionais, incluindo casas e apartamentos em bairros residenciais no Brasil e em mais 190 países.

**Beautiful Soup** é uma biblioteca Python de extração de dados de arquivos HTML e XML. Ela funciona com o seu interpretador (parser) favorito a fim de prover maneiras mais intuitivas de navegar, buscar e modificar uma árvore de análise (parse tree).


### Map e Reduce em Aquário

Neste projeto vamos utilizar a função **reduce** combinada com a **map** para realizarmos a contagem de quantos animais existem no aquário para cada tipo (estamos mencionando um dos projetos realizados anteriormente: **Filtrando e Mapeando Animais de um Aquário**). Será uma ótima oportunidade de trabalhar com o conceito de Map Reduce utilizado por diversos frameworks de processamento de dados, como Hadoop MapREduce e Apache Spark. 

O **MapReduce** nada mais é do que um modelo de programação, uma forma de escrever algoritmos que foi proposto pelo Google para processar grandes volumes de dados (Big Data). O MapReduce é baseado em conceitos da programação funcional. Trabalhando também com a estrutura de tupla, lendo um arquivo que estava em outro diretório. 

### Conversor de Moedas Orientado a Objetos

Nesse experimento vamos construir um conversor de moedas, em que o usuário informa a quantidade em valor e a moeda inicial com qual a moeda destino desejada (se tenho cem reais quantos euros consigo compra? quantos doláres consigo comprar). O programa devolve ao usuário o resultado dessa conversão. Essa solucução será construída trabalhando com Programação orientada à objetos e utilizando uma API gratuita para coletar dados em relação à moedas em diversos lugares do mundo. Ou seja, esse projeto visa trazer uma introdução de forma prática do conceito de **Programação orientada à objetos**. Como se trata de uma API GRATUITA é para fins de teste e está sujeita a tempos de inatividade. Senso assim devemos usar com cuidado e evitar abusar para que outros também possam usá-lo corretamente. Vamos usar essa API: https://free.currencyconverterapi.com/ que é uma api simples e objetiva para conversão de moeda. 


### Portas Lógicas e Herança (Em andamento)

O objetivo nesse projeto é colocar em prática o conceito de herança dentro do paradigma de Programação Orientada a Objetos. O contexto foi simular o funcionamento de portas lógicas tendo a implementação baseada nesse conceito. 

Herança é um princípio de programação orientada a objetos, que permite que classes compartilhem atributos e métodos, através de "heranças". Ela é usada na intenção de reaproveitar código ou comportamento generalizado ou especializar operações ou atributos. Ponto importante é que a herança ocorre de cima pra baixo, ou seja, se uma classe é a primeira, a mesma não consegue herdar da última. 


### Gerenciador de senha

Nesse projeto a ideia é construir um gerador de senha.

Podemos nos perguntar: É seguro usar gerenciador de senha? Dentro desse contexto o risco mais claro de usar um gerenciador de senhas é que ele mantém todas as suas informações confidenciais de login em um só lugar. Sendo assim, uma violção pode ser catastrófica. É por isso que muitos gerenciadores de senhas usam várias camadas de segurança, que reduzem bastante a chance de suas senhas serem vazadas. 


### Respondendo Usuário

Nesse projeto a ideia é criar um programa que leia o nome de uma pessoa, usuário e mostrar uma mensagem de boas-vindas.

### Somando dois números

Será criado um programa que leia dois números e mostre a soma entre eles. 

### Dissecando uma Variável

Neste, será desenvolvido um programa que recebe uma entrada do usuário através do teclado e exibe na tela seu tipo primitivo e todas as informações disponíveis sobre ele.


### Antecessor e Sucessor

Será criado nesse projeto, um programa que leia um número inteiro e mostre na tela o seu antecessor e sucessor. Aqui é possível observar também á aplicação de algumas funções: **Print** e **Input**.


### Dobro, Triplo e Raiz Quadrada

Nesse caso, será criado um algoritmo, programa que leia um número e mostre o seu dobro, triplo e raiz quadrada. Aplicando inclusive a função **sqrt()** do módulo mat, que é útil para calcular raiz quadrada de um número, retornando a raiz quadrada comom um valor de ponto flutuante. 


### Calculo e Média 

Nesse projeto, será desenvolvido um programa que lerá as duas notas de um aluno, calculará e mostrará a sua média aritmética. Serão utilizadas duas condicionais **if** (se) e **else** (se não) para enriquecer ainda mais o programa.




