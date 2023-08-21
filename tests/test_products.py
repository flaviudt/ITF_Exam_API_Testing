"""
Teste pentru endpoint-urile de products
din https://dummyjson.com/docs/products.

Aceste teste folosesc metodele ajutatoare
definite in clasa ProductsRequests,
pentru a interactiona cu API-ul.
"""
import unittest

from dummyjson_requests.products import ProductsRequests


class TestProductsRequests(unittest.TestCase):

    def setUp(self):
        self.products_req = ProductsRequests()

    def test_get_all_products(self):
        """
        Verificari:
        - status code = 200
        - in raspunsul json, am primit exact 30 de produse
        - cheia total are valoarea 100
        - cheia limit are valoarea 30
        - cheia skip are valoarea 0
        """
        response = self.products_req.get_products()
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_msg["products"]), 30)
        self.assertEqual(response_msg["total"], 100)
        self.assertEqual(response_msg["limit"], 30)
        self.assertEqual(response_msg["skip"], 0)

    def test_get_products_when_limit_is_set(self):
        """
        Verificari:
        - status code este 200
        - in raspunsul json, am primit exact <limit> de produse
        - cheia limit are valoarea <limit>
        """
        limit = 10
        response = self.products_req.get_products(limit=limit)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_msg["products"]), limit)
        self.assertEqual(response_msg["limit"], limit)

    def test_get_products_when_skip_is_set(self):
        """
        Verificari:
        - status code este 200
        - in raspunsul json, verificam ca id-ul primului produs
        este <skip + 1>
        - cheia skip are valoarea <skip>
        """
        skip = 5
        response = self.products_req.get_products(skip=skip)
        response_msg = response.json()
        product_id = response_msg["products"][0]["id"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(product_id, skip + 1)
        self.assertEqual(response_msg["skip"], skip)

    def test_get_products_when_skip_is_greater_than_total_number_of_products(self):
        """
        Verificari:
        - status code este 200
        - in raspunsul json, avem cheia products, dar valoarea acesteia, este o lista goala.
        - cheia skip are valoarea <skip>
        """
        skip = 200
        response = self.products_req.get_products(skip=skip)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response_msg["products"])
        self.assertEqual(response_msg["skip"], skip)

    def test_get_products_when_skip_has_invalid_format(self):
        """
        Verificari:
        - status code este 400
        - verificam ca mesajul primit in response este cel asteptat
        """
        skip = "invalid"
        response = self.products_req.get_products(skip=skip)
        response_msg = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_msg["message"], "Invalid skip limit")

    def test_get_product_by_id_when_id_is_in_db(self):
        """
        Verificari:
        - status code este 200
        - in raspuns, ca pentru cheia id, avem aceeasi valoare, ca cea trimisa in request
        - verificam ca avem cheile: title, price, description, category,stock in response
        """
        response = self.products_req.get_product_by_id(4)
        response_msg = response.json()
        keys_list = ["title", "price", "description", "category", "stock"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], 4)
        for key in keys_list:
            self.assertIn(key, response_msg)

    def test_get_product_by_id_when_id_is_not_in_db(self):
        """
        Verificari:
        - status code este 404
        - in raspuns, verificam mesajul
        """
        product_id = 110
        response = self.products_req.get_product_by_id(product_id=product_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_msg["message"], f"Product with id '{product_id}' not found")

    def test_search_product_when_products_found_by_criteria(self):
        """
        Verificari:
        - status code 200
        - verificam ca lista products NU este goala
        - total > 0
        - limit > 0
        """
        search = "phone"
        response = self.products_req.search_products(search=search)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_msg["products"])
        self.assertGreater(response_msg["total"], 0)
        self.assertGreater(response_msg["limit"], 0)

    def test_search_product_when_products_not_found_by_criteria(self):
        """
        Verificari:
        - status code 200
        - verificam ca lista products este goala
        - total este egal cu 0
        - limit este egal cu 0
        """
        search = "phonee"
        response = self.products_req.search_products(search=search)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response_msg["products"])
        self.assertEqual(response_msg["total"], 0)
        self.assertEqual(response_msg["limit"], 0)

    def test_add_product_with_single_key(self):
        """
        Verificari:
        - status code = 200
        - id = 101
        - title in response message
        """
        body = {"title": "BW Pencil"}
        response = self.products_req.add_product(**body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], 101)
        self.assertIn("title", response_msg)

    def test_add_product_with_multiple_keys(self):
        """
        Verificari:
        - status code = 200
        - id = 101
        - title, stock, price in response message
        """
        body = {
            "title": "BW Pencil",
            "stock": 1000,
            "price": 300
        }
        response = self.products_req.add_product(**body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], 101)
        self.assertIn("title", response_msg)
        self.assertIn("stock", response_msg)
        self.assertIn("price", response_msg)

    def test_add_product_with_invalid_key(self):
        """
        Verificari:
        - status code = 200
        - id = 101
        """
        body = {"101": 100}
        response = self.products_req.add_product(**body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], 101)

    def test_update_product(self):
        """
        Verificari:
        - status code = 200
        - id = id
        - stock = 1000
        """
        body = {
            "title": "iPhone Galaxy +1",
            "stock": 1000
        }
        product_id = 1
        response = self.products_req.update_product(product_id=product_id, **body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], product_id)
        self.assertEqual(response_msg["stock"], 1000)

    def test_delete_product_when_id_is_in_db(self):
        """
        Verificari:
        - status code = 200
        - id = id
        - "isDeleted" = true
        """
        product_id = 3
        response = self.products_req.delete_product(product_id=product_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], product_id)
        self.assertEqual(response_msg["isDeleted"], True)

    def test_delete_product_when_id_is_not_in_db(self):
        """
        Verificari:
        - status code = 404
        - "message" = "Product with id '300' not found"
        """
        product_id = 300
        response = self.products_req.delete_product(product_id=product_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_msg["message"], "Product with id '300' not found")

