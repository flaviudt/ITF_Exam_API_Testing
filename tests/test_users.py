import unittest

from dummyjson_requests.users import UsersRequests


class TestUsersRequests(unittest.TestCase):
    def setUp(self):
        self.users_req = UsersRequests()

    def test_get_all_users(self):
        """
        Verificari:
        - status code = 200
        - in raspunsul json, am primit exact 30 de useri
        - cheia total are valoarea 100
        - cheia limit are valoarea 30
        - cheia skip are valoarea 0
        """
        response = self.users_req.get_all_users()
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_msg["users"]), 30)
        self.assertEqual(response_msg["total"], 100)
        self.assertEqual(response_msg["limit"], 30)
        self.assertEqual(response_msg["skip"], 0)

    def test_get_user_by_id(self):
        """
        - status code = 200
        - response id = id
        - avem in raspuns firstName, lastName, age
        """
        user_id = 5
        response = self.users_req.get_user_by_id(user_id=user_id)
        response_msg = response.json()
        key_list = ["firstName", "lastName", "age"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], user_id)
        for key in key_list:
            self.assertIn(key, response_msg)

    def test_search_users(self):
        """
        Verificari:
        - status code = 200
        - verificam ca lista nu e goala
        - veficam ca total > 0
        """
        search = "Mavis"
        response = self.users_req.search_users(search=search)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_msg["users"])
        self.assertGreater(response_msg["total"], 0)

    def test_get_user_carts_by_user_id(self):
        """
        Verificari:
        - statsus code = 200
        """
        user_id = 5
        response = self.users_req.get_user_carts_by_user_id(user_id=user_id)
        self.assertEqual(response.status_code, 200)

    def test_get_user_posts_by_user_id(self):
        """
        Verificari:
        - statsus code = 200
        - verificam ca lista nu e goala
        """
        user_id = 5
        response = self.users_req.get_user_posts_by_user_id(user_id=user_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_msg["posts"])

    def test_get_user_todos_by_user_id(self):
        """
        Verificari:
        - statsus code = 200
        - verificam ca lista nu e goala
        - total > 0
        """
        user_id = 5
        response = self.users_req.get_user_todos_by_user_id(user_id=user_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_msg["todos"])
        self.assertGreater(response_msg["total"], 0)

    def test_add_new_user(self):
        """
        Verificari:
        - status code = 200
        - id = 101
        - age = 25
        """
        body = {
            "id": 101,
            "firstName": "Muhammad",
            "lastName": "Ovi",
            "age": 25
        }
        response = self.users_req.add_new_user(**body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], 101)
        self.assertEqual(response_msg["age"], 25)

    def test_update_user(self):
        """
        Verificari:
        - status code = 200
        - id = id
        """
        user_id = 5
        body = {
            "age": 50
        }
        response = self.users_req.update_user(user_id=user_id, **body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], 5)

    def test_delete_user(self):
        """
        Verificari:
        - status code = 200
        - id = id
        - "isDeleted" = true
        """
        user_id = 3
        response = self.users_req.delete_user(user_id=user_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], user_id)
        self.assertEqual(response_msg["isDeleted"], True)
    