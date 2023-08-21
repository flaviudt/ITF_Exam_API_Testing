import requests


class CommentsRequests:
    _BASE_URL = "https://dummyjson.com/comments"

    def get_all_comments(self, limit=None, skip=None, select=None):
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

    def get_comment_by_id(self, comment_id):
        url = f"{self._BASE_URL}/{comment_id}"
        response = requests.get(url)
        return response

    def get_all_comments_by_post_id(self, post_id):
        url = f"{self._BASE_URL}/post/{post_id}"
        response = requests.get(url)
        return response

    def add_comment(self, **kwargs):
        url = f"{self._BASE_URL}/add"
        response = requests.post(url, json=kwargs)
        return response

    def update_comment(self, comment_id, **kwargs):
        url = f"{self._BASE_URL}/{comment_id}"
        response = requests.patch(url, json=kwargs)
        return response

    def delete_comment(self, comment_id):
        url = f"{self._BASE_URL}/{comment_id}"
        response = requests.delete(url)
        return response
