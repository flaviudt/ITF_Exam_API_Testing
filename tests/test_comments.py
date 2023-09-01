import unittest

from dummyjson_requests.comments import CommentsRequests


class TestCommentsRequests(unittest.TestCase):

    def setUp(self):
        self.comments_req = CommentsRequests()

    def test_get_all_comments(self):
        """
        Verificari:
        - status code = 200
        - cheia total = 340
        """
        response = self.comments_req.get_all_comments()
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["total"], 340)

    def test_get_all_comments_with_limit_and_skip(self):
        """
        Verificari:
        - status code = 200
        - cheia limit = 20
        - cheia skip = 10
        - id-ul primului 'comment' = 11
        """
        limit = 20
        skip = 10
        response = self.comments_req.get_all_comments(limit=limit, skip=skip)
        response_msg = response.json()
        comment_id = response_msg["comments"][0]["id"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["limit"], limit)
        self.assertEqual(response_msg["skip"], skip)
        self.assertEqual(comment_id, skip + 1)

    def test_get_comment_by_id(self):
        """
        Verificari:
        - status code = 200
        - id = comment_id
        - verificam ca avem cheile: id, body, postId, user
        """
        comment_id = 5
        response = self.comments_req.get_comment_by_id(comment_id=comment_id)
        response_msg = response.json()
        keys_list = ["id", "body", "postId", "user"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], comment_id)
        for key in keys_list:
            self.assertIn(key, response_msg)

    def test_get_comment_by_id_when_id_is_not_in_db(self):
        """
        Verificari:
        - status code = 404
        - message = Comment with id '4000' not found
        """
        comment_id = 4000
        response = self.comments_req.get_comment_by_id(comment_id=comment_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_msg["message"], f"Comment with id '{comment_id}' not found")

    def test_get_all_comments_by_post_id(self):
        """
        Verificari:
        - status code = 200
        - total > 0
        """
        post_id = 5
        response = self.comments_req.get_all_comments_by_post_id(post_id=post_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertGreater(response_msg["total"], 0)

    def test_add_comment(self):
        """
          Verificari:
          - status code = 200
          - id = 341
          - postId = 3
        """
        body = {
            "body": "yes.you di IT",
            "postId": 3,
            "userId": 5
        }
        response = self.comments_req.add_comment(**body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], 341)
        self.assertEqual(response_msg["postId"], 3)

    def test_update_comment(self):
        """
          Verificari:
          - status code = 200
          - id = comment_id
          - postId = 1
          - userId = 6
          - username = jtreleven5
        """
        body = {
            "body": "Updated comment",
            "postId": 1,
            "userId": 6
        }
        comment_id = 15
        response = self.comments_req.update_comment(comment_id=comment_id, **body)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], 15)
        self.assertEqual(response_msg["postId"], 1)
        self.assertEqual(response_msg["user"]["id"], 6)
        self.assertEqual(response_msg["user"]["username"], "jtreleven5")

    def test_delete_comment(self):
        """
        Verificari:
        - status code = 200
        - id = comment_id
        - "isDeleted" = true
        """
        comment_id = 3
        response = self.comments_req.delete_comment(comment_id=comment_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], comment_id)
        self.assertEqual(response_msg["isDeleted"], True)
