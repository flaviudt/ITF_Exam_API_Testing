import unittest

from dummyjson_requests.posts import PostsRequests


class TestPostsRequests(unittest.TestCase):

    def setUp(self):
        self.posts_req = PostsRequests()

    def test_get_all_posts(self):
        """
        Verificari:
        - status code = 200
        - cheia total = 150
        """
        response = self.posts_req.get_all_posts()
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["total"], 150)

    def test_get_all_posts_when_limit_and_skip_is_set(self):
        """
        Verificari:
        - status code = 200
        - cheia limit = 8
        - cheia skip = 3
        - id-ul primului 'post' = 4
        """
        limit = 8
        skip = 3
        response = self.posts_req.get_all_posts(limit=limit, skip=skip)
        response_msg = response.json()
        post_id = response_msg["posts"][0]["id"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["limit"], limit)
        self.assertEqual(response_msg["skip"], skip)
        self.assertEqual(post_id, skip + 1)

    def test_get_post_by_id(self):
        """
        Verificari:
        - status code = 200
        - in raspuns, ca pentru cheia id, avem aceeasi valoare, ca
        cea trimisa in request
        - verificam ca avem cheile: title, body, tags, reactions
        """
        post_id = 5
        response = self.posts_req.get_post_by_id(post_id=post_id)
        response_msg = response.json()
        keys_list = ["title", "body", "tags", "reactions"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], post_id)
        for key in keys_list:
            self.assertIn(key, response_msg)

    def test_search_post(self):
        """
        Verificari:
        - status code = 200
        - verificam ca lista posts NU este goala
        - total > 0
        - limit > 0
        """
        search = "secrets"
        response = self.posts_req.search_post(search=search)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_msg["posts"])
        self.assertGreater(response_msg["total"], 0)
        self.assertGreater(response_msg["limit"], 0)

    def test_get_posts_by_user_id(self):
        """
        Verificari:
        - status code = 200
        - total > 0
        """
        user_id = 8
        response = self.posts_req.get_posts_by_user_id(user_id=user_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertGreater(response_msg["total"], 0)

    def test_get_comments_of_a_post(self):
        """
        Verificari:
        - status code = 200
        - total = 6
        """
        post_id = 3
        response = self.posts_req.get_post_comments(post_id=post_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["total"], 6)

    def test_add_post(self):
        """
          Verificari:
          - status code = 200
          - id = 151
        """
        body = {
            "title": "New Post By Me",
            "userId": 1
        }
        response = self.posts_req.add_post(**body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], 151)

    def test_add_post_without_userid(self):
        """
          Verificari:
          - status code = 400
          - message = User id is required
        """
        body = {
            "title": "Not Working"
        }
        response = self.posts_req.add_post(**body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_msg["message"], "User id is required")

    def test_delete_post(self):
        """
        Verificari:
        - status code = 200
        - id = id
        - "isDeleted" = true
        """
        post_id = 1
        response = self.posts_req.delete_post(post_id=post_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], post_id)
        self.assertEqual(response_msg["isDeleted"], True)









