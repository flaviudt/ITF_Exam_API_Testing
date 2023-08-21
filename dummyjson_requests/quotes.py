import requests


class QuotesRequests:
    _BASE_URL = "https://dummyjson.com/quotes"

    def get_all_quotes(self, limit=None, skip=None):
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

    def get_a_single_quote(self, quote_id):
        url = f"{self._BASE_URL}/{quote_id}"
        response = requests.get(url)
        return response

    def get_a_random_quote(self):
        url = f"{self._BASE_URL}/random"
        response = requests.get(url)
        return response
