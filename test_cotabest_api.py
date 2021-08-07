#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import unittest
from cotabest_api import app
from werkzeug.wrappers import response

class FlaskTestCase(unittest.TestCase):
    """ Classe responsável pelos testes unitários da aplicação em Flask
    """
    def setUp(self):
        """ Teste inicial
        """
        app.config['TESTING'] = True
        self.test_app = app.test_client()


    def test_api_list_products_200(self):
        """ Teste da rota /api/list_products que lista os produtos disponíveis
        """
        response = self.test_app.get('/api/list_products')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.content_type, 'application/json')


    def test_api_find_products_200(self):
        """ Teste da rota /api/find_products quando uma palavra possui maiúsculas e o parâmetro name é passado corretamente
        """
        payload = json.dumps({
            'name': 'reFri'
        })

        expected_return = b'[{"amount-per-package":12,"id":3,"max-availability":150000,"minimun":120,"name":"Refrigerante","price":1.0}]\n'

        response = self.test_app.post('/api/find_products', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_find_products_400(self):
        """ Teste da rota /api/find_products quando uma palavra possui maiúsculas e o parâmetro name é passado incorretamente
        """
        payload = json.dumps({
            'nam': 'reFri'
        })

        expected_return = b'{"error":"O par\\u00e2metro name n\\u00e3o foi informado!!!"}\n'

        response = self.test_app.post('/api/find_products', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_shopping_cart_200(self):
        """ Teste da rota /api/shopping_cart que exibe o carrinho de compras
        """
        response = self.test_app.get('/api/shopping_cart')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.content_type, 'application/json')


    def test_api_add_shopping_cart_400_id(self):
        """ Teste da rota /api/add_shopping_cart quando o parâmetro id é passado incorretamente
        """
        payload = json.dumps({
            "id": 10,
            "quantity": 120
        })

        expected_return = b'{"error":"O par\\u00e2metro id n\\u00e3o foi informado ou n\\u00e3o foi encontrado !!!"}\n'

        response = self.test_app.post('/api/add_shopping_cart', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_add_shopping_cart_400_quantity(self):
        """ Teste da rota /api/add_shopping_cart quando o parâmetro quantity é passado incorretamente
        """
        payload = json.dumps({
            "id": 3,
            "quanity": 120
        })

        expected_return = b'{"error":"O par\\u00e2metro quantity n\\u00e3o foi informado !!!"}\n'

        response = self.test_app.post('/api/add_shopping_cart', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_add_shopping_cart_200(self):
        """ Teste da rota /api/add_shopping_cart quando o parâmetro id e quantity são passados e validados corretamente
        """
        payload = json.dumps({
            "id": 3,
            "quantity": 120
        })

        expected_return = b'{"sucess":"O produto Refrigerante com 120 unidades foi adicionado com sucesso !!!"}\n'

        response = self.test_app.post('/api/add_shopping_cart', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_add_shopping_cart_400_in_shopping_cart(self):
        """ Teste da rota /api/add_shopping_cart quando o o produto já foi inserido no carrinho
        """
        payload = json.dumps({
            "id": 3,
            "quantity": 120
        })

        expected_return = b'{"error":["O produto Refrigerante j\\u00e1 foi inserido no carrinho compras !!!"]}\n'

        response = self.test_app.post('/api/add_shopping_cart', data=payload, content_type='application/json')
        response = self.test_app.post('/api/add_shopping_cart', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_update_shopping_cart_400_id(self):
        """ Teste da rota /api/update_shopping_cart quando o parâmetro id é passado incorretamente
        """
        payload = json.dumps({
            "id": 10,
            "quantity": 120
        })

        expected_return = b'{"error":"O par\\u00e2metro id n\\u00e3o foi informado ou n\\u00e3o foi encontrado !!!"}\n'

        response = self.test_app.put('/api/update_shopping_cart', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_update_shopping_cart_400_quantity(self):
        """ Teste da rota /api/update_shopping_cart quando o parâmetro quantity é passado incorretamente
        """
        payload = json.dumps({
            "id": 3,
            "quanity": 120
        })

        expected_return = b'{"error":"O par\\u00e2metro quantity n\\u00e3o foi informado !!!"}\n'

        response = self.test_app.put('/api/update_shopping_cart', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_update_shopping_cart_200(self):
        """ Teste da rota /api/update_shopping_cart quando o parâmetro id e quantity são passados e validados corretamente
        """
        payload = json.dumps({
            "id": 3,
            "quantity": 120
        })

        expected_return = b'{"sucess":"O produto Refrigerante com 120 unidades foi adicionado com sucesso !!!"}\n'

        response = self.test_app.post('/api/add_shopping_cart', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)

        payload = json.dumps({
            "id": 3,
            "quantity": 240
        })

        expected_return = b'{"sucess":"O produto Refrigerante foi atualizado com sucesso para 240 unidades !!!"}\n'

        response = self.test_app.put('/api/update_shopping_cart', data=payload, content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_update_shopping_cart_400_not_in_shopping_cart(self):
        """ Teste da rota /api/update_shopping_cart quando o produto não estava cadastrado no carrinho de compras
        """
        payload = json.dumps({
            "id": 2,
            "quantity": 120
        })

        expected_return = b'{"error":["O produto Ra\\u00e7\\u00e3o para coelho n\\u00e3o est\\u00e1 cadastrado no carrinho compras !!!"]}\n'

        response = self.test_app.put('/api/update_shopping_cart', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_remove_shopping_cart_400_id(self):
        """ Teste da rota /api/remove_shopping_cart quando o parâmetro id é passado incorretamente
        """
        payload = json.dumps({
            "id": 10,
            "quantity": 120
        })

        expected_return = b'{"error":"O par\\u00e2metro id n\\u00e3o foi informado ou n\\u00e3o foi encontrado !!!"}\n'

        response = self.test_app.delete('/api/remove_shopping_cart', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_remove_shopping_cart_200(self):
        """ Teste da rota /api/remove_shopping_cart quando o parâmetro id é passado e validado corretamente
        """
        payload = json.dumps({
            "id": 3,
            "quantity": 120
        })

        expected_return = b'{"sucess":"O produto Refrigerante com 120 unidades foi adicionado com sucesso !!!"}\n'

        response = self.test_app.post('/api/add_shopping_cart', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)

        payload = json.dumps({
            "id": 3
        })

        expected_return = b'{"sucess":"O produto Refrigerante foi removido do carrinho com sucesso !!!"}\n'

        response = self.test_app.delete('/api/remove_shopping_cart', data=payload, content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_remove_shopping_cart_400_not_in_shopping_cart(self):
        """ Teste da rota /api/remove_shopping_cart quando o produto não está cadastrado no carrinho de compras
        """
        payload = json.dumps({
            "id": 3
        })

        expected_return = b'{"error":["O produto Refrigerante n\\u00e3o est\\u00e1 cadastrado no carrinho compras !!!"]}\n'

        response = self.test_app.delete('/api/remove_shopping_cart', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_checkout_400_empty_shopping_cart(self):
        """ Teste da rota /api/checkout quando o carrinho de compras está vazio
        """
        expected_return = b'{"error":"N\\u00e3o existe nenhum produto no carrinho !!!"}\n'

        response = self.test_app.get('/api/checkout')
        self.assertEqual(response.status_code, 400)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)


    def test_api_checkout_200(self):
        """ Teste da rota /api/checkout que finaliza a compra e limpa o carrinho de compras
        """
        payload = json.dumps({
            "id": 4,
            "quantity": 120
        })

        expected_return = b'{"sucess":"O produto Feij\\u00e3o preto com 120 unidades foi adicionado com sucesso !!!"}\n'

        response = self.test_app.post('/api/add_shopping_cart', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.content_type, 'application/json')
        self.assertEqual(response.data, expected_return)
       
        response = self.test_app.get('/api/checkout')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()