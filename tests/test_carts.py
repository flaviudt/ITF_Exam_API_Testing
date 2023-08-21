import unittest

from dummyjson_requests.carts import CartsRequests


class TestCartsRequests(unittest.TestCase):

    def setUp(self):
        self.carts_req = CartsRequests()

    def test_get_all_carts(self):
        """
        Verificari:
        - status code = 200
        - cheia total = 20
        - cheia limit = 20
        """
        response = self.carts_req.get_all_carts()
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["total"], 20)
        self.assertEqual(response_msg["limit"], 20)

    def test_get_cart_by_id_when_id_is_in_db(self):
        """
        Verificari:
        - status code = 200
        - response id = id
        - avem in raspuns discountedTotal, totalProducts
        """
        cart_id = 1
        response = self.carts_req.get_cart_by_id(cart_id=cart_id)
        response_msg = response.json()
        key_list = ["discountedTotal", "totalProducts"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], cart_id)
        for key in key_list:
            self.assertIn(key, response_msg)

    def test_get_cart_by_id_when_id_is_not_in_db(self):
        """
        Verificari:
        - status code = 404
        - in raspuns, verificam mesajul
        """
        cart_id = 99
        response = self.carts_req.get_cart_by_id(cart_id=cart_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_msg["message"], f"Cart with id '{cart_id}' not found")

    def test_get_carts_of_a_user_with_carts(self):
        """
        Verificari:
        - status code = 200
        """
        user_id = 5
        response = self.carts_req.get_carts_of_a_user(user_id=user_id)
        self.assertEqual(response.status_code, 200)

    def test_get_carts_of_a_user_without_carts(self):
        """
        Verificari:
        - status code = 200
        - no carts
        - cheia total = 0
        """
        user_id = 55
        response = self.carts_req.get_carts_of_a_user(user_id=user_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response_msg["carts"])
        self.assertEqual(response_msg["total"], 0)

    def test_add_cart(self):
        """
        Verificari:
        - status code = 200
        - id = 21
        - products in response message
        """
        body = {
            "id": 21,
            "products": [
                {
                    "id": 1,
                    "title": "iPhone 9",
                    "price": 549,
                    "quantity": 1,
                    "total": 549,
                    "discountPercentage": 12.96,
                    "discountedPrice": 478
                },
                {
                    "id": 50,
                    "title": "Women Shoes",
                    "price": 36,
                    "quantity": 2,
                    "total": 72,
                    "discountPercentage": 16.87,
                    "discountedPrice": 60
                }
            ],
            "total": 621,
            "discountedTotal": 538,
            "userId": 1,
            "totalProducts": 2,
            "totalQuantity": 3
        }
        response = self.carts_req.add_cart(**body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], 21)
        self.assertIn("products", response_msg)

    def test_update_cart(self):
        """
        Verificari:
        - status code = 200
        - id = id
        - total = 549
        """
        body = {
            "products": [
                {
                    "id": 1,
                    "title": "iPhone 9",
                    "price": 549,
                    "quantity": 1,
                    "total": 549,
                    "discountPercentage": 12.96,
                    "discountedPrice": 478
                }
            ],
            "total": 3798,
            "discountedTotal": 3172,
            "userId": 97,
            "totalProducts": 6,
            "totalQuantity": 11
        }
        cart_id = 2
        response = self.carts_req.update_cart(cart_id=cart_id, **body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], cart_id)
        self.assertEqual(response_msg["total"], 549)

    def test_delete_cart(self):
        """
        Verificari:
        - status code = 200
        - id = id
        - "isDeleted" = true
        """
        cart_id = 5
        response = self.carts_req.delete_cart(cart_id=cart_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], cart_id)
        self.assertEqual(response_msg["isDeleted"], True)
