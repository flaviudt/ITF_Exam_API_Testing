import unittest

from dummyjson_requests.quotes import QuotesRequests


class TestQuotesRequests(unittest.TestCase):

    def setUp(self):
        self.quotes_req = QuotesRequests()

    def test_get_all_qoutes(self):
        """
        Verificari:
        - status code = 200
        - cheia total = 100
        """
        response = self.quotes_req.get_all_quotes()
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["total"], 100)

    def test_get_quote_by_id(self):
        """
        Verificari:
        - status code = 200
        - id = quote_id
        - author = Albert Einstein
        """
        quote_id = 3
        response = self.quotes_req.get_a_single_quote(quote_id=quote_id)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["id"], quote_id)
        self.assertEqual(response_msg["author"], "Albert Einstein")

    def test_get_quotes_with_limit_and_skip_set(self):
        """
        Verificari:
        - status code = 200
        - cheia limit = limit
        - cheia skip = skip
        - autorul primului citat e Steve Jobs
        """
        limit = 5
        skip = 20
        response = self.quotes_req.get_all_quotes(limit=limit, skip=skip)
        response_msg = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_msg["limit"], limit)
        self.assertEqual(response_msg["skip"], skip)
        self.assertEqual(response_msg["quotes"][0]["author"], "Steve Jobs")

    def test_get_random_quote(self):
        """
        Verificari:
        - status code = 200
        - verificam ca avem cheile: id, quote, author
        """
        response = self.quotes_req.get_a_random_quote()
        response_msg = response.json()
        keys_list = ["id", "quote", "author"]
        self.assertEqual(response.status_code, 200)
        for key in keys_list:
            self.assertIn(key, response_msg)
