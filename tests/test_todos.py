import unittest

from dummyjson_requests.todos import TodosRequests


class TestTodosRequests(unittest.TestCase):

    def setUp(self):
        self.todos_req = TodosRequests()

    def test_get_all_todos(self):
        """
        Verificari:
        - status code = 200
        - cheia total = 150
        """
        response = self.todos_req.get_all_todos()
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["total"], 150)

    def test_get_todo_by_id(self):
        """
        Verificari:
        - status code = 200
        - id = todo_id
        - completed = False
        - userId = 1
        """
        todo_id = 17
        response = self.todos_req.get_a_single_todo(todo_id=todo_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["completed"], False)
        self.assertEqual(response_msg["userId"], 1)

    def test_get_random_todo(self):
        """
        Verificari:
        - status code = 200
        - verificam ca avem cheile: id, to-do, completed, userId
        """
        response = self.todos_req.get_a_random_todo()
        response_msg = response.json()
        keys_list = ["id", "todo", "completed", "userId"]
        self.assertEqual(response.status_code, 200)
        for key in keys_list:
            self.assertIn(key, response_msg)

    def test_get_all_todos_by_user_id(self):
        """
        Verificari:
        - status code = 200
        - total = 2
        - completed = false
        """
        user_id = 10
        response = self.todos_req.get_all_todos_by_user_id(user_id=user_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["total"], 2)
        self.assertEqual(response_msg["todos"][0]["completed"], False)
        self.assertEqual(response_msg["todos"][1]["completed"], False)

    def test_add_todo(self):
        """
          Verificari:
          - status code = 200
          - id = 151
          - userId = 5
          - completed = False
        """
        body = {
            "id": 151,
            "todo": "Use DummyJSON in the project",
            "completed": False,
            "userId": 5
        }
        response = self.todos_req.add_a_new_todo(**body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], 151)
        self.assertEqual(response_msg["userId"], 5)
        self.assertEqual(response_msg["completed"], False)

    def test_update_todo(self):
        """
          Verificari:
          - status code = 200
          - id = todo_id
          - completed = True
          - userId = 26
        """
        body = {
            "todo": "This is an updated Todo",
            "completed": True,
        }
        todo_id = 1
        response = self.todos_req.update_todo(todo_id=todo_id, **body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], todo_id)
        self.assertEqual(response_msg["completed"], True)
        self.assertEqual(response_msg["userId"], 26)

    def test_delete_todo(self):
        """
        Verificari:
        - status code = 200
        - id = todo_id
        - "isDeleted" = true
        """
        todo_id = 3
        response = self.todos_req.delete_todo(todo_id=todo_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], todo_id)
        self.assertEqual(response_msg["isDeleted"], True)

