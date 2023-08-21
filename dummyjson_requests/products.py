"""
Clasa cu metode ajutatoare pentru a interactiona cu un API
prin care obtinem date despre produse
"""

import requests


class ProductsRequests:
    _BASE_URL = "https://dummyjson.com/products"

    def get_products(self, limit=None, skip=None, select=None):
        products_url = self._BASE_URL
        param_dict = {}

        if limit is not None:
            param_dict.update({"limit": limit})
        if skip is not None:
            param_dict.update({"skip": skip})
        if select is not None:
            param_dict.update({"select": select})
        if len(param_dict) != 0:
            response = requests.get(products_url, params=param_dict)
        else:
            response = requests.get(products_url)
        return response

    def get_product_by_id(self, product_id):
        url = f"{self._BASE_URL}/{product_id}"
        response = requests.get(url)
        return response

    def search_products(self, search):
        url = self._BASE_URL + f"/search?q={search}"
        response = requests.get(url)
        return response

    def get_product_categories(self):
        url = f"{self._BASE_URL}/categories"
        response = requests.get(url)
        return response

    def get_products_of_category(self, category_name):
        url = self._BASE_URL + f"/categories/{category_name}"
        response = requests.get(url)
        return response

    def add_product(self, **kwargs):
        url = f"{self._BASE_URL}/add"
        response = requests.post(url, json=kwargs)
        return response

    def update_product(self, product_id, **kwargs):
        url = f"{self._BASE_URL}/{product_id}"
        response = requests.patch(url, json=kwargs)
        return response

    def delete_product(self, product_id):
        url = f"{self._BASE_URL}/{product_id}"
        response = requests.delete(url)
        return response
