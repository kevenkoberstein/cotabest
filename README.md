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
