#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
from os import error
from libs import classes as cls


def read_products_list():
    """ Função que retorna a lista de produtos contida no arquivo JSON de exemplo

    Returns:
        [list]: Retorna a lista de produtos
    """
    # Abre o JSON e salva em uma lista
    with open('./docs/data.json') as json_file:
        products = json.load(json_file)

    return products


def find_products(name:str, products:list):
    """ Função responsável por encontrar um produto na lista de produtos através do seu nome

    Args:
        name (str): Nome ou parte do nome do produto
        products (list): Lista de produtos

    Returns:
        [list]: Retorna a lista de produtos com o nome informado
    """
    matches = []

    # Varre a lista de produtos
    for product in products:
        # Caso encontre correspondência adiciona na lista de matches
        if product['name'].find(name) != -1:
            matches.append(product)

    return matches


def get_shopping_cart(shopping_cart:cls.Shopping_Cart):
    """ Função que retorna o carrinho de compras atual

    Args:
        shopping_cart (cls.Shopping_Cart): Carrinho de Compras

    Returns:
        [dict]: Retorna um dicionário de dados contendo os items e o preço total
    """
    total_price = shopping_cart.total_price
    items = []

    # Varrendo a lista e formatando para um dicionário
    for product in shopping_cart.items:
        var = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'minimun': product.minimun,
            'amount_per_package': product.amount_per_package,
            'max_availability': product.max_availability,
            'quantity': product.quantity 
        }

        items.append(var)

    data = {
        'total-price': total_price,
        'items': items
    }
    
    return data


def find_product_by_id(id:int, products:list):
    """ Função responsável por encontrar um produto na lista de produtos através do seu id

    Args:
        id (int): Id do produto
        products (list): Lista de produtos

    Returns:
        [dict]: Retorna um produto com base no id informado
    """
    match = False

    # Varre a lista de produtos
    for product in products:
        # Caso encontre correspondência na lista de produtos
        if product['id'] == id:
            match = product

    return match


def return_error_messages(errors:dict, item:cls.Item):
    """ Função responsável por retornar as mensagens de erro

    Args:
        errors (list): Lista de erros

    Returns:
        [list]: Retorna uma lista com os erros encontrados
    """
    current_messages = []

    error_messages = {
        'in_shopping_cart': 'O produto {0} já foi inserido no carrinho compras !!!'.format(item.name),
        'not_in_shopping_cart': 'O produto {0} não está cadastrado no carrinho compras !!!'.format(item.name),
        'verify_minimun': 'O produto {0} não atingiu a quantidade mínima de {1} unidades !!!'.format(item.name, item.minimun),
        'verify_amount_per_package': 'O produto {0} não atingiu a quantidade por pacote de {1} unidades !!! Faltam {2} unidades na quantidade para solucionar o problema!!!',
        'verify_max_availability': 'O produto {0} ultrapassou a quantidade máxima de {1} unidades disponíveis em estoque!!!'.format(item.name, item.max_availability)
    }

    # Varre a lista de erros e adiciona as mensagens
    for error in errors:
        if type(error) == str:
            current_messages.append(error_messages[error])
        else:
            current_messages.append(error_messages['verify_amount_per_package'].format(item.name, item.amount_per_package, error['verify_amount_per_package'][2]))

    data = {
        'error': current_messages 
    }

    return(data)