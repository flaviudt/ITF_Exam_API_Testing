import requests


class CartsRequests:
    _BASE_URL = "https://dummyjson.com/carts"

    def get_all_carts(self):
        url = self._BASE_URL
        response = requests.get(url)
        return response

    def get_cart_by_id(self, cart_id):
        url = f"{self._BASE_URL}/{cart_id}"
        response = requests.get(url)
        return response

    def get_carts_of_a_user(self, user_id):
        url = f"{self._BASE_URL}/user/{user_id}"
        response = requests.get(url)
        return response

    def add_cart(self, **kwargs):
        url = f"{self._BASE_URL}/add"
        response = requests.post(url, json=kwargs)
        return response

    def update_cart(self, cart_id, **kwargs):
        url = f"{self._BASE_URL}/{cart_id}"
        response = requests.patch(url, json=kwargs)
        return response

    def delete_cart(self, cart_id):
        url = f"{self._BASE_URL}/{cart_id}"
        response = requests.delete(url)
        return response

