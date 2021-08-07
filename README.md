# Cotabest

Neste documento temos um manual dos procedimentos necessários para o funcionamento do Teste Técnico Dev Backend da Cotabest em um ambiente de produção. A fim de cumprir com os requisitos propostos no teste temos um sistema de backend utilizando Flask, e devidamente documentado nas seções seguintes.

# Preparando Ambiente Virtual (venv)

Como primeira etapa para o funcionamento do projeto temos a utilização de um ambiente virtual. Alguns comandos básicos foram listados abaixo para relembrar os procedimentos necessários no ambiente de produção. Uma cópia da venv também está contida no projeto, e pode ser utilizada caso necessário.

## `Criando a venv`

Caso seja necessário você pode criar a venv python no servidor com o comando abaixo.

``` bash
python3 -m venv cotabest-env
```

## `Entrando na venv`

Para entrar na venv, caso ela já esteja criada, basta digitar o comando a seguir.
``` bash
source cotabest-env/bin/activate
```

## `Criando a lista de pacotes instalados na venv`

Para criar a lista de pacotes intaladdos na venv basta rodar o seguinte comando.

``` bash
pip freeze > requirements.txt
```

## `Instalando a lista de pacotes necessários para o funcionamento da venv`

Para instalar os pacotes necessários para o funcionamento do projeto no ambiente de produção, temos o comando abaixo.

``` bash
python -m pip install -r requirements.txt
```

# Rodando a aplicação

Para rodar a aplicação basta executar o comando abaixo.

``` bash
python cotabest_api.py
```

# Documentação da API

A documentação dos métodos aceitos, rotas, exemplos foi feita utilizando o Postman e está disponível online para consulta no endereço a seguir

> https://documenter.getpostman.com/view/16981531/Tzsimjdy

# Testes unitários da API

Os testes unitários da API em Flask estão no script `test_cotabest_api.py`. Seria possível realizar testes unitários para cada função e classe, presente na pasta libs, porém para simplificar foram aplicados apenas testes na API diretamente em vista do prazo. O comando para rodar os testes, com o percentual de cobertura dos testes está inserido abaixo e deve ser rodado dentro da pasta principal.

``` bash
python -m pytest --cov=cotabest_api
```

Abaixo temos um exemplo do resultado do testes realizados
``` bash
================================================================================ test session starts =================================================================================
platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /home/visin/cotabest
plugins: cov-2.12.1
collected 17 items                                                                                                                                                                   

test_cotabest_api.py .................                                                                                                                                         [100%]

---------- coverage: platform linux, python 3.8.10-final-0 -----------
Name              Stmts   Miss  Cover
-------------------------------------
cotabest_api.py      78      1    99%
-------------------------------------
TOTAL                78      1    99%


================================================================================= 17 passed in 0.34s =================================================================================
```

# Considerações

* Apesar da API possuir varias rotas para visualizar, adicionar, atualizar, e remover os itens do carrinho seria possível fazer todo esse procedimento em apenas uma rota. O que não foi implementado por não constar nos requisitos.
* Não foi definido um requisito de qual identificador deveria ser utilizado para adicionar, atualizar, e remover os itens do carrinho, logo por convenção e boa prática adotou-se o id das soluções.
* Como não foram definidas as mensagens de erro a serem enviadas para o usuário, por convenção o nome do produto foi apresentado, ao invés do id dentro da mensagem.
* Os únicos itens que podem ser adicionados no carrinho são os que estão presentes no arquivo de JSON base.
* Conforme os requisitos não havia a necessidade de utilização de uma base de dados, logo a mesma não foi implementada.
* Para o item 3, onde o sistema deveria atender a quantidade miníma antes de finalizar a compra, foi verificada uma incoerência no requisito. Pois essa validação deve ser feita quando o usuário adiciona ou atualiza a quantidade de um produto, pois não há sentido em adicionar algo que esteja fora de uma das regras de negócio. Logo a validação de quantidade mínima foi alterada para ser feita antes do usuário chegar no procedimento de finalizar a compra.
* Para a questão onde temos que a quantidade de items deve bater com a quantidade vendida por pacote, temos um retorno da api na qual o item não é adicionado no carrinho, mas há uma sugestão para o usuário de quantos items ele deve inserir a fim de atender a regra de negócio.
* Foi obtido um percentual de cobertura de teste unitários na API de 99%.