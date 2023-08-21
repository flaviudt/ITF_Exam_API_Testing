import requests


class TodosRequests:
    _BASE_URL = "https://dummyjson.com/todos"

    def get_all_todos(self, limit=None, skip=None):
        url = self._BASE_URL
        param_dict = {}
        if limit is not None:
            param_dict.update({"limit": limit})
        if skip is not None:
            param_dict.update({"skip": skip})
        if len(param_dict) != 0:
            response = requests.get(url, params=param_dict)
        else:
            response = requests.get(url)
        return response

    def get_a_single_todo(self, todo_id):
        url = f"{self._BASE_URL}/{todo_id}"
        response = requests.get(url)
        return response

    def get_a_random_todo(self):
        url = f"{self._BASE_URL}/random"
        response = requests.get(url)
        return response

    def get_all_todos_by_user_id(self, user_id):
        url = f"{self._BASE_URL}/user/{user_id}"
        response = requests.get(url)
        return response

    def add_a_new_todo(self, **kwargs):
        url = f"{self._BASE_URL}/add"
        response = requests.post(url, json=kwargs)
        return response

    def update_todo(self, todo_id, **kwargs):
        url = f"{self._BASE_URL}/{todo_id}"
        response = requests.patch(url, json=kwargs)
        return response

    def delete_todo(self, todo_id):
        url = f"{self._BASE_URL}/{todo_id}"
        response = requests.delete(url)
        return response




