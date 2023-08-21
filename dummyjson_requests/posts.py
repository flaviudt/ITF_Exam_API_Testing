import requests


class PostsRequests:
    _BASE_URL = "https://dummyjson.com/posts"

    def get_all_posts(self, limit=None, skip=None, select=None):
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

    def get_post_by_id(self, post_id):
        url = f"{self._BASE_URL}/{post_id}"
        response = requests.get(url)
        return response

    def search_post(self, search):
        url = f"{self._BASE_URL}/search?q={search}"
        response = requests.get(url)
        return response

    def get_posts_by_user_id(self, user_id):
        url = f"{self._BASE_URL}/user/{user_id}"
        response = requests.get(url)
        return response

    def get_post_comments(self, post_id):
        url = f"{self._BASE_URL}/{post_id}/comments"
        response = requests.get(url)
        return response

    def add_post(self, **kwargs):
        url = f"{self._BASE_URL}/add"
        response = requests.post(url, json=kwargs)
        return response

    def update_post(self, post_id, **kwargs):
        url = f"{self._BASE_URL}/{post_id}"
        response = requests.patch(url, json=kwargs)
        return response

    def delete_post(self, post_id):
        url = f"{self._BASE_URL}/{post_id}"
        response = requests.delete(url)
        return response
