#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import uuid
from flask import Flask, request, jsonify
from libs import classes as cls
from libs import functions as funcs

app = Flask(__name__)

# Criando um carrinho de compras
shopping_cart_1 = cls.Shopping_Cart()

# item_1 = cls.Item(1, "teste_1", 10.0, 5, 5, 100, 10)
# item_2 = cls.Item(2, "teste_2", 1.0, 10, 5, 200, 20)

# shopping_cart_1.add_to_shopping_cart(item_1)
# shopping_cart_1.add_to_shopping_cart(item_2)

@app.route('/api/list_products', methods=['GET','POST'])
def list_products():
    """ Rota da api que retorna a lista de produtos

    Returns:
        [json]: Retorna a lista de produtos cadastrados no arquivo JSON de base
    """
    products = funcs.read_products_list()
    return jsonify(products), 200


@app.route('/api/find_products', methods=['POST'])
def find_products():
    """ Rota da api que retorna um produto com base no nome informado

    Returns:
        [json]: Retorna a lista de produtos encontrados com o nome informado, ou erro caso o parâmetro name não seja informado
    """
    name = request.json.get('name')
    
    # Caso o parâmetro name tenha sido passado corretamente retorna os matches
    if name is not None:
        products = funcs.read_products_list()
        matches = funcs.find_products(name, products)
        return jsonify(matches), 200

    else:
        # Caso o parâmetro name não tenha sido passado corretamente
        return jsonify({'error': 'O parâmetro name não foi informado!!!'}), 400


@app.route('/api/shopping_cart', methods=['GET'])
def get_shopping_cart():
    """ Rota da api que exibe o carrinho de compras

    Returns:
        [json]: Retorna os dados presentes no carrinho de compras
    """
    global shopping_cart_1

    data = funcs.get_shopping_cart(shopping_cart_1)
    return jsonify(data), 200


@app.route('/api/add_shopping_cart', methods=['POST'])
def add_to_shopping_cart():
    """ Rota da api que verifica se o produto existe no arquivo de JSON, validando as informações necessárias, e adicionando no carrinho

    Returns:
        [json]: Retorna se um produto foi criado ou os erros que foram encontrados
    """    
    global shopping_cart_1
    
    id = request.json.get('id')
    quantity = request.json.get('quantity')
    products = funcs.read_products_list()
    match = funcs.find_product_by_id(id, products)

    # Caso não seja passado um id ou não encontre o produto
    if id is None or not match:
        # Caso o parâmetro name não tenha sido passado corretamente
        return jsonify({'error': 'O parâmetro id não foi informado ou não foi encontrado !!!'}), 400 

    # Caso não seja passada a quantidade
    if quantity is None:
        # Caso o parâmetro name não tenha sido passado corretamente
        return jsonify({'error': 'O parâmetro quantity não foi informado !!!'}), 400   

    item = cls.Item(match['id'], match['name'], match['price'], match['minimun'], match['amount-per-package'], match['max-availability'], quantity)
    add_cart = shopping_cart_1.add_to_shopping_cart(item)

    # Caso não encontre erros
    if add_cart == True:
        return jsonify({'sucess': 'O produto {0} com {1} unidades foi adicionado com sucesso !!!'.format(item.name, item.quantity)}), 200

    # Pegando as mensagens de erro a serem exibidas
    errors = funcs.return_error_messages(add_cart, item)

    return jsonify(errors), 400


@app.route('/api/update_shopping_cart', methods=['POST'])
def update_to_shopping_cart():
    """ Rota da api que verifica se o produto existe no carrinho, validando as informações necessárias, e atualizando seu valor

    Returns:
        [json]: Retorna se um produto foi atualizado ou os erros que foram encontrados
    """
    global shopping_cart_1

    id = request.json.get('id')
    quantity = request.json.get('quantity')
    products = funcs.read_products_list()
    match = funcs.find_product_by_id(id, products)

    # Caso não seja passado um id ou não encontre o produto
    if id is None or not match:
        # Caso o parâmetro name não tenha sido passado corretamente
        return jsonify({'error': 'O parâmetro id não foi informado ou não foi encontrado !!!'}), 400 

    # Caso não seja passada a quantidade
    if quantity is None:
        # Caso o parâmetro name não tenha sido passado corretamente
        return jsonify({'error': 'O parâmetro quantity não foi informado !!!'}), 400   

    item = cls.Item(match['id'], match['name'], match['price'], match['minimun'], match['amount-per-package'], match['max-availability'], quantity)
    update_cart = shopping_cart_1.update_to_shopping_cart(item)

    # Caso não encontre erros
    if update_cart == True:
        return jsonify({'sucess': 'O produto {0} foi atualizado com sucesso para {1} unidades !!!'.format(item.name, item.quantity)}), 200

    # Pegando as mensagens de erro a serem exibidas
    errors = funcs.return_error_messages(update_cart, item)

    return jsonify(errors), 400


@app.route('/api/remove_shopping_cart', methods=['POST'])
def remove_from_shopping_cart():
    """ Rota da api que verifica se o produto existe no carrinho de compras, e caso exista remove

    Returns:
        [json]: Retorna se um produto foi removido ou os erros que foram encontrados
    """
    global shopping_cart_1

    id = request.json.get('id')
    products = funcs.read_products_list()
    match = funcs.find_product_by_id(id, products)

    # Caso não seja passado um id ou não encontre o produto
    if id is None or not match:
        # Caso o parâmetro name não tenha sido passado corretamente
        return jsonify({'error': 'O parâmetro id não foi informado ou não foi encontrado !!!'}), 400 

    item = cls.Item(match['id'], match['name'], match['price'], match['minimun'], match['amount-per-package'], match['max-availability'], 0)
    remove_cart = shopping_cart_1.remove_from_shopping_cart(item)

    # Caso não encontre erros
    if remove_cart == True:
        return jsonify({'sucess': 'O produto {0} foi removido do carrinho com sucesso !!!'.format(item.name)}), 200

    # Pegando as mensagens de erro a serem exibidas
    errors = funcs.return_error_messages(remove_cart, item)

    return jsonify(errors), 400


@app.route('/api/checkout', methods=['GET'])
def checkout():
    """ Rota da api que finaliza a compra, gerando um id de pedido, e zerando o carrinho

    Returns:
        [json]: Retorna se um produto foi removido ou os erros que foram encontrados
    """
    global shopping_cart_1

    data = funcs.get_shopping_cart(shopping_cart_1)

    print(data)

    # Caso não tenha nenhum produto no carrinho
    if data == {'total-price': 0, 'items': []}:
        return jsonify({'error': 'Não existe nenhum produto no carrinho !!!'}), 400 
    
    # Gerando o id de pedido
    data['id'] = uuid.uuid4()

    # Zerando o carrinho de compras
    shopping_cart_1 = cls.Shopping_Cart()
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)