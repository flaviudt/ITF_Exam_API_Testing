import requests


class UsersRequests:
    _BASE_URL = "https://dummyjson.com/users"

    def get_all_users(self, limit=None, skip=None, select=None):
        url = self._BASE_URL
        param_dict = {}
        if limit is not None:
            param_dict.update({"limit": limit})
        if skip is not None:
            param_dict.update({"skip": skip})
        if select is not None:
            param_dict.update({"select": select})
        if len(param_dict) != 0:
            response = requests.get(url, params=param_dict)
        else:
            response = requests.get(url)
        return response

    def get_user_by_id(self, user_id):
        url = f"{self._BASE_URL}/{user_id}"
        response = requests.get(url)
        return response

    def search_users(self, search):
        url = f"{self._BASE_URL}/search?q={search}"
        response = requests.get(url)
        return response

    def filter_users(self, key, value):
        url = f"{self._BASE_URL}/filer?key={key}&value={value}"
        response = requests.get(url)
        return response

    def get_user_carts_by_user_id(self, user_id):
        url = f"{self._BASE_URL}/{user_id}/carts"
        response = requests.get(url)
        return response

    def get_user_posts_by_user_id(self, user_id):
        url = f"{self._BASE_URL}/{user_id}/posts"
        response = requests.get(url)
        return response

    def get_user_todos_by_user_id(self, user_id):
        url = f"{self._BASE_URL}/{user_id}/todos"
        response = requests.get(url)
        return response

    def add_new_user(self, **kwargs):
        url = f"{self._BASE_URL}/add"
        response = requests.post(url, json=kwargs)
        return response

    def update_user(self, user_id, **kwargs):
        url = f"{self._BASE_URL}/{user_id}"
        response = requests.patch(url, json=kwargs)
        return response

    def delete_user(self, user_id):
        url = f"{self._BASE_URL}/{user_id}"
        response = requests.delete(url)
        return response
