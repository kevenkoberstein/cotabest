#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Item:
    """ Classe responsável pela criação dos produtos e seus atributos
    """
    def __init__(self, id:int, name:str, price:float, minimun:int, amount_per_package:int, max_availability:int, quantity:int):
        """ Função que cria o produto com os valores padrão passados por parâmetro

        Args:
            id (int): Identificador do produto
            name (str): Nome do produto
            price (float): Preço do produto
            minimun (int): Quantidade mínima de produto a ser vendida
            amount_per_package (int): Quantidade a ser vendida por pacote
            max_availability (int): Quantidade máxima disponível em estoque
            quantity (int): Quantidade a ser colocada no carrinho de compras
        """
        self.__id = id
        self.__name = name
        self.__price = price
        self.__minimun = minimun
        self.__amount_per_package = amount_per_package
        self.__max_availability = max_availability
        self.__quantity = quantity

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def minimun(self):
        return self.__minimun

    @property
    def amount_per_package(self):
        return self.__amount_per_package

    @property
    def max_availability(self):
        return self.__max_availability

    @property
    def quantity(self):
        return self.__quantity

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @price.setter
    def price(self, price):
        self.__price = price

    @minimun.setter
    def minimun(self, minimun):
        self.__minimun = minimun

    @amount_per_package.setter
    def amount_per_package(self, amount_per_package):
        self.__amount_per_package = amount_per_package

    @max_availability.setter
    def max_availability(self, max_availability):
        self.__max_availability = max_availability    

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity


class Shopping_Cart:
    """ Classe que responsável por criar, e manipular o carrinho de compras
    """
    def __init__(self):
        self.__items = []
        self.__total_price = 0

    @property
    def items(self):
        return self.__items

    @property
    def total_price(self):
        total = 0
        for item in self.items:
            total = total + (item.price * item.quantity)
        
        self.__total_price = total
        return self.__total_price

    def in_shopping_cart(self, Item:Item):
        """ Função que retorna a posição caso encontre o item informado no carrinho

        Args:
            Item (Item): Produto

        Returns:
            [int]: Retorna a posição dentro do carrinho, caso o produto seja encontrado
        """
        pos = -1
        for index, product in enumerate(self.__items):
            if Item.id == product.id:
                pos = index
        return pos

    def verify_minimun(self, Item:Item):
        """ Função que valida se a quantidade mínima foi atingida

        Args:
            Item (Item): Produto

        Returns:
            [bool]: Retorna verdadeiro caso a quantidade mínima seja atingida
        """
        verify = False
        if (Item.quantity >= Item.minimun):
            verify = True
        return verify

    def verify_amount_per_package(self, Item:Item):
        """ Função que valida se a quantidade está compatível com a quantidade por pacote

        Args:
            Item (Item): Produto

        Returns:
            [list]: Retorna uma lista contendo o resto da divisão, o quociente, e quanto de produto falta para completar um pacote
        """
        dividend = Item.quantity
        divider = Item.amount_per_package
        quotient = dividend // divider
        rest = dividend % divider
        missing = divider - rest
        return rest, quotient, missing

    def verify_max_availability(self, Item:Item):
        """ Função que valida se a quantidade não ultrapassa a quantidade em estoque

        Args:
            Item (Item): Produto

        Returns:
            [bool]: Retorna verdadeiro caso a quantidade informada esteja disponível em estoque
        """
        verify = False
        if (Item.quantity > 0) and (Item.quantity <= Item.max_availability):
            verify = True
        return verify

    def add_to_shopping_cart(self, Item:Item):
        """ Função que adiciona um item no carrinho

        Args:
            Item (Item): Produto

        Returns:
            [bool]: Retorna verdadeiro caso não encontre nenhum erro
            or
            [list]: Retorna uma lista com todos os erros encontrados
        """
        errors = []

        # Verifica se o item já está no carrinho
        in_shopping_cart = self.in_shopping_cart(Item)

        if in_shopping_cart != -1:
            errors.append("in_shopping_cart")

        # Verifica se o item atingiu a quantidade mínima
        verify_minimun = self.verify_minimun(Item)

        if not verify_minimun:
            errors.append("verify_minimun")

        # Verifica se a quantidade está compatível com a quantidade por pacote
        verify_amount_per_package = self.verify_amount_per_package(Item)

        if verify_amount_per_package[0] != 0:
            errors.append({"verify_amount_per_package": verify_amount_per_package})

        # Verifica se a quantidade não ultrapassa a quantidade em estoque
        verify_max_availability = self.verify_max_availability(Item)

        if not verify_max_availability:
            errors.append("verify_max_availability")

        # Caso seja encontrado algum erro
        if errors != []:
            return errors

        # Caso atenda a todos os requisitos adiciona o item no carrinho
        self.__items.append(Item)

        return True

    def update_to_shopping_cart(self, Item:Item):
        """ Função que atualiza um item do carrinho

        Args:
            Item (Item): Produto

        Returns:
            [bool]: Retorna verdadeiro caso não encontre nenhum erro
            or
            [list]: Retorna uma lista com todos os erros encontrados
        """
        errors = []

        # Verifica se o item está no carrinho
        in_shopping_cart = self.in_shopping_cart(Item)

        if in_shopping_cart == -1:
            errors.append("not_in_shopping_cart")

        # Verifica se o item atingiu a quantidade mínima
        verify_minimun = self.verify_minimun(Item)

        if not verify_minimun:
            errors.append("verify_minimun")

        # Verifica se a quantidade está compatível com a quantidade por pacote
        verify_amount_per_package = self.verify_amount_per_package(Item)

        if verify_amount_per_package[0] != 0:
            errors.append({"verify_amount_per_package": verify_amount_per_package})

        # Verifica se a quantidade não ultrapassa a quantidade em estoque
        verify_max_availability = self.verify_max_availability(Item)

        if not verify_max_availability:
            errors.append("verify_max_availability")

        # Caso seja encontrado algum erro
        if errors != []:
            return errors

        # Caso atenda a todos os requisitos adiciona o item no carrinho
        self.__items[in_shopping_cart].quantity = Item.quantity

        return True

    # Função que remove um item do carrinho
    def remove_from_shopping_cart(self, Item:Item):
        """ Função que remove um item do carrinho

        Args:
            Item (Item): Produto

        Returns:
            [bool]: Retorna verdadeiro caso não encontre nenhum erro
            or
            [list]: Retorna uma lista com todos os erros encontrados
        """
        errors = []

        # Verifica se o item está no carrinho
        in_shopping_cart = self.in_shopping_cart(Item)

        if in_shopping_cart == -1:
            errors.append("not_in_shopping_cart")

        # Caso seja encontrado algum erro
        if errors != []:
            return errors

        # Caso atenda a todos os requisitos adiciona o item no carrinho
        del[self.__items[in_shopping_cart]]

        return True




# shopping_cart_1 = Shopping_Cart()

# # (id, name, price, minimun, amount_per_package, max_availability, quantity)
# item_1 = Item(1, "blar", 10.0, 5, 5, 100, 10)
# item_2 = Item(2, "xablauzinho", 1.0, 10, 5, 200, 20)
# item_3 = Item(1, "blar", 10.0, 5, 5, 100, 20)

# shopping_cart_1.add_to_shopping_cart(item_1)
# shopping_cart_1.add_to_shopping_cart(item_2)

# print(shopping_cart_1.items)
# print(shopping_cart_1.total_price)

# shopping_cart_1.remove_from_shopping_cart(item_2)

# print(shopping_cart_1.items)
# print(shopping_cart_1.total_price)


# print(shopping_cart_1.update_to_shopping_cart(item_3))

# print(shopping_cart_1.items)
# print(shopping_cart_1.total_price)